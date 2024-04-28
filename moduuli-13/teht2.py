from flask import Flask
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="python_pilot",
    user="root",
    password="admin",
    autocommit=True
)
@app.route('/kenttä/<icao>', methods=['GET'])
def kenttä(icao):
    sql = "SELECT ident, municipality from airport where ident=%s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    mytiedot = kursori.fetchall()
    return mytiedot

if __name__ == '__main__':
    app.run(port=3000)