import os
import psycopg2

conn = psycopg2.connect(

        host        = "ec2-34-235-31-124.compute-1.amazonaws.com",
        database    = "d87b79k4h2v8ll",
        user        = "tmzuihdcumyntq",
        password    = "4429cf39d83cb78718a7b9e5f7e623835ae603c26e7d187bb15d300be0d73790",
        port        = "5432"
        )
cur = conn.cursor()

cur.execute("CREATE TABLE TblMovie(Id int, Name varchar(100), year int, date_creation date DEFAULT CURRENT_TIMESTAMP)")
conn.commit()