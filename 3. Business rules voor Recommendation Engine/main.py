import psycopg2, csv

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
            segment varchar
        );
        CREATE TABLE content_recs(
            prodid varchar,
            segment varchar
        );
        ALTER TABLE collab_recs 
        ADD FOREIGN KEY (prodid) REFERENCES products(id);
        
        ''')
conn.commit()


# Collaborative Filtering
def get_segments():
    segments = []
    query = '''
    SELECT segment FROM sessions 
    GROUP BY segment'''
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        segment = row[0]
        if segment not in segments:
            segments.append(segment)
    return segments


def collab_filter_recommendations():
    recommendations = {}
    segments = get_segments()
    for segment in segments:
        if segment is not None:
            recommendations[segment] = []
            query = f'''
                SELECT count(prodid), prodid FROM profiles_previously_viewed
                WHERE profid in (
                    SELECT id FROM profiles
                    WHERE segment = '{segment}'
                )
                GROUP BY prodid
                ORDER BY count(prodid) DESC
                LIMIT 3'''
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                recommendations[segment].append(row[1])
    return recommendations


def fill_colab_filter_csv(filename):
    recommendations = collab_filter_recommendations()
    with open(filename, 'w', newline='') as collab:
        collab_fieldnames = ['prodid', 'segment']
        collab_writer = csv.DictWriter(collab, fieldnames=collab_fieldnames)
        collab_writer.writeheader()
        for segment in recommendations:
            for product in recommendations[segment]:
                collab_writer.writerow(
                    {
                        'prodid': product,
                        'segment': segment
                    }
                )


def fill_colab_filter_db(filename):
    fill_colab_filter_csv(filename)
    with open(filename, 'r') as collab:
        next(collab)
        cur.copy_from(collab, 'collab_recs', sep=',')
        conn.commit()
    conn.close()


fill_colab_filter_db('collab_recs.csv')
