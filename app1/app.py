from flask import Flask, render_template, url_for, redirect, request
import my_lists
from main import Person
import psycopg2

conn = psycopg2.connect("dbname=some_personal_db user=postgres password=admin123" )
cur = conn.cursor()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/fill_form")
def forms():
    return render_template("forms.html", cities = my_lists.cities )

@app.route("/register", methods = ["POST"])
def register():
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    address = request.form.get("address")
    city = request.form.get("my_city")
    newPerson = Person(fname, lname, address, city)

    cur.execute('INSERT INTO persons VALUES (newPerson.id, newPerson.l_name, newPerson.f_name, newPerson.address, newPerson.city)')
    # fullname = fname + lname

    return render_template("hello.html", foo = fullname)



if __name__ == "__main__":
    app.run(debug=True)