import os
import psycopg2

conn = psycopg2.connect(

        host        = 'localhost',
        database    = "mymovie_db",
        user        = "postgres",
        password    = '461775'
        )

cur = conn.cursor()

cur.execute("CREATE TABLE TblMovie(Id int, Name varchar(100), year int, date_creation date DEFAULT CURRENT_TIMESTAMP)")
conn.commit()