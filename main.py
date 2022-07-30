from flask import Flask, request
from flask import render_template, redirect
import psycopg2


# DATABASE_URL: postgres://tmzuihdcumyntq:4429cf39d83cb78718a7b9e5f7e623835ae603c26e7d187bb15d300be0d73790@ec2-34-235-31-124.compute-1.amazonaws.com:5432/d87b79k4h2v8l
# heroku config --app movieproject007

conn = psycopg2.connect(

        host        = "ec2-34-235-31-124.compute-1.amazonaws.com",
        database    = "d87b79k4h2v8l",
        user        = "tmzuihdcumyntq",
        password    = "4429cf39d83cb78718a7b9e5f7e623835ae603c26e7d187bb15d300be0d73790",
        port        = "5432"
        )

cur = conn.cursor()

app = Flask(__name__)

#this function is used for geeting data from database
@app.route("/")
def main():
    movie_list = []
    #getting data from database
    cur.execute("SELECT * from TblMovie")
    movie_data = cur.fetchall()
    print("movie_data", movie_data)
    for mov in movie_data:
        movie_dict = {  "movie_id"      :   mov[0],
                        "movie_title"   :   mov[1],
                        "movie_year"    :   mov[2]
                    }
        movie_list.append(movie_dict)

    print("movie_list", movie_list)
        
    return render_template('movielist.html', movie_list = movie_list)

@app.route("/addmovie", methods = ['GET', 'POST'])
def addmovie():
    if request.method == "GET":
        return render_template("addmovie.html", movie_update_list = {})
    elif request.method == "POST":
        id      =       request.form["id"]
        print("id", id)
        title   =       request.form["title"]
        print("title", title)
        year    =       request.form["year"]
        print("year", year)

        #inserting data in our database
        cur.execute('INSERT INTO TblMovie (id, name, year)'
        'VALUES (%s, %s, %s)', (id, title, year))
        conn.commit()
        return redirect('/')

@app.route("/updatemovie/<int:id>", methods = ['GET', 'POST', "PUT"])
def updatemovie(id):
        movie_update_list = []    
        if request.method == "GET":
            cur.execute(f"SELECT * from TblMovie where id = {id}")
            movie_data = cur.fetchall()
            print("movie_data", movie_data)
            for mov in movie_data:
                movie_dict = {  "movie_id"      :   mov[0],
                                "movie_title"   :   mov[1],
                                "movie_year"    :   mov[2]
                            }
            movie_update_list.append(movie_dict)
            return render_template("addmovie.html", movie_update_list = movie_update_list[0])

        elif request.method == "POST":
            id      =       request.form["id"]
            print("id", id)
            title   =       request.form["title"]
            print("title", title)
            year    =       request.form["year"]
            print("year", year)
            year    =       request.form["year"]
            cur.execute(f"UPDATE TblMovie SET id = '{id}', name = '{title}', year = '{year}' WHERE id = {id}")
            conn.commit()

            print("movie_update_list", movie_update_list)

            return redirect('/')


        


@app.route("/deletemovie/<int:id>", methods = ['GET', 'POST', "DELETE"])
def deletemovie(id):
    print("del id", id)
    cur.execute("DELETE FROM TblMovie WHERE id = {}".format(str(id)))
    return redirect('/')
   


if __name__ == '__main__':
   app.run(debug=True)




    #    cur.execute('INSERT INTO TblMovie (Id, Name, year)'
    # 'VALUES (%s, %s, %s)', (1, 'Life is Beautiful', 1985))
    # conn.commit()