import os
from dotenv import load_dotenv
import psycopg2
load_dotenv()


conn = psycopg2.connect(
        host="localhost",
        database="moviedb",
        user=os.environ.get('DB_USERNAME'),
        password=os.environ.get('DB_PASSWORD'))

# Open a cursor to perform database operations
cur = conn.cursor()


cur.execute("CREATE TABLE TblMovie(Id int, Name varchar(100), year int, date_creation date DEFAULT CURRENT_TIMESTAMP)")
conn.commit()