import pymongo, psycopg2, csv

client = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDB = client["huwebshop"]

hostname = 'localhost'
username = 'postgres'
password = 'Floris09'
database = 'huwebshop'

conn = psycopg2.connect(host=hostname, user=username, password=password, database=database)
cur = conn.cursor()

cur.execute('''
        DROP TABLE IF EXISTS collab_recs;
        DROP TABLE IF EXISTS content_recs;
        ''')

