'''
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun.
'''

import mysql.connector
from geopy.distance import geodesic


def fetch_data(a, b):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE airport.ident = '{a}' OR airport.ident = '{b}'"
    cursor = db_connection.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    calc_dist(res)


def calc_dist(res):
    a = (res[0][0], res[0][1])
    b = (res[1][0], res[1][1])

    dist = geodesic(a, b).kilometers
    print("Lentokenttien etäisyys: ", round(dist), "km")


db_connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="admin",
    autocommit=True
)

first = input("Syötä ensimmäisen lentokentän ICAO-tunnus: ")
second = input("Syötä toisen lentokentän ICAO-tunnus: ")

fetch_data(first, second)