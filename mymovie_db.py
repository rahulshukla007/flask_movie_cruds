import os
import psycopg2

conn = psycopg2.connect(

        host        = "ec2-34-235-31-124.compute-1.amazonaws.com",
        database    = "d87b79k4h2v8ll",
        user        = "tmzuihdcumyntq",
cur = conn.cursor()

cur.execute("CREATE TABLE TblMovie(Id int, Name varchar(100), year int, date_creation date DEFAULT CURRENT_TIMESTAMP)")
conn.commit()