import psycopg2, csv, random

hostname = 'localhost'
username = 'postgres'
password = 'Floris09'
database = 'huwebshop'

conn = psycopg2.connect(host=hostname, user=username, password=password, database=database)
cur = conn.cursor()

cur.execute('''
        DROP TABLE IF EXISTS collab_recs;
        DROP TABLE IF EXISTS content_recs;
        CREATE TABLE collab_recs(
            prodid varchar,
            segment varchar,
            devicetype varchar
        );
        CREATE TABLE content_recs(
            prodid varchar,
            prodids varchar
        );
        ALTER TABLE collab_recs 
        ADD FOREIGN KEY (prodid) REFERENCES products(id);
        ALTER TABLE content_recs 
        ADD FOREIGN KEY (prodid) REFERENCES products(id);
        
        ''')
conn.commit()


# Collaborative Filtering op basis van segment en device type
def get_segments():
    segments = []
    device_types = []
    segment_query = '''
        SELECT segment FROM sessions 
        GROUP BY segment'''
    device_type_query = '''
        SELECT devicetype FROM sessions
        GROUP BY devicetype'''
    cur.execute(segment_query)
    rows = cur.fetchall()
    for row in rows:
        segment = row[0]
        if segment not in segments:
            segments.append(segment)
    cur.execute(device_type_query)
    rows = cur.fetchall()
    for row in rows:
        device_type = row[0]
        if device_type not in device_types:
            device_types.append(device_type)
    segments_devices = []
    for segment in segments:
        for device_type in device_types:
            if device_type is not None and segment is not None:
                segments_devices.append(segment + ":" + device_type)
    return segments_devices


def collab_filter_recommendations():
    recommendations = {}
    segments_devices = get_segments()
    for segment_device in segments_devices:
        segment = segment_device.split(':')[0]
        device = segment_device.split(':')[1]
        if segment is not None and device is not None:

            index = segment + ":" + device
            recommendations[index] = []
            query = f'''
                SELECT count(prodid), prodid FROM profiles_previously_viewed
                WHERE profid in (
                    SELECT profiles.id
                    FROM sessions
                    INNER JOIN profiles ON sessions.profid=profiles.id
                    WHERE profiles.segment = '{segment}'
                    AND sessions.devicetype = '{device}'
                )
                GROUP BY prodid
                ORDER BY count(prodid) DESC
                LIMIT 3'''
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                recommendations[index].append(row[1])
    return recommendations


def fill_colab_filter_csv(filename):
    recommendations = collab_filter_recommendations()
    with open(filename, 'w', newline='') as collab:
        collab_fieldnames = ['prodid', 'segment', 'devicetype']
        collab_writer = csv.DictWriter(collab, fieldnames=collab_fieldnames)
        collab_writer.writeheader()
        for segment in recommendations:
            for product in recommendations[segment]:
                collab_writer.writerow(
                    {
                        'prodid': product,
                        'segment': segment.split(':')[0],
                        'devicetype': segment.split(':')[1]
                    }
                )


def fill_colab_filter_db(filename):
    fill_colab_filter_csv(filename)
    with open(filename, 'r') as collab:
        next(collab)
        cur.copy_from(collab, 'collab_recs', sep=',')
        conn.commit()


# Content Filtering op basis van category, subcategory en subsubcategory

def get_all_products():
    products = {}
    query = '''
        SELECT id, category, subcategory, subsubcategory, targetaudience FROM products'''
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        products[row[0]] = {
            'cat': row[1],
            'subcat': row[2],
            'subsubcat': row[3],
            'ta': row[4]
        }
    return products


def get_content_recs():
    products = get_all_products()
    recommendations = {}
    for product in products:
        cat = products[product]['cat']
        subcat = products[product]['subcat']
        subsubcat = products[product]['subcat']
        cat_recs = []
        subcat_recs = []
        subsubcat_recs = []
        for rec_product in products:
            if rec_product != product:
                if products[rec_product]['cat'] == cat:
                    cat_recs.append(rec_product)
                    if products[rec_product]['subcat'] == subcat:
                        subcat_recs.append(rec_product)
                        if products[rec_product]['subsubcat'] == subsubcat:
                            subsubcat_recs.append(rec_product)
        if len(subsubcat_recs) >= 3:
            recs = random.sample(subsubcat_recs, 3)
        elif len(subcat_recs) >= 3:
            recs = random.sample(subcat_recs, 3)
        elif len(cat_recs) >= 3:
            recs = random.sample(cat_recs, 3)
        else:
            recs = random.sample(list(products.keys()), 3)
        recommendations[product] = recs
    return recommendations


def fill_content_filter_csv(filename):
    recommendations = get_content_recs()
    with open(filename, 'w', newline='') as content:
        content_fieldnames = ['prodid', 'prodids']
        content_writer = csv.DictWriter(content, fieldnames=content_fieldnames)
        content_writer.writeheader()
        for product in recommendations:
            content_writer.writerow(
                {
                    'prodid': product,
                    'prodids': ';'.join(recommendations[product])
                }
            )


def fill_content_filter_db(filename):
    fill_content_filter_csv(filename)
    with open(filename, 'r') as content:
        next(content)
        cur.copy_from(content, 'content_recs', sep=',')
        conn.commit()


# Run content filtering
fill_content_filter_db('content_recs.csv')
# Run collaborative filtering
fill_colab_filter_db('collab_recs.csv')
conn.close()
