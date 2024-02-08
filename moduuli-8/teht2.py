'''
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

'''

import mysql.connector


def fetch_data(code):
    sql = f'SELECT name, type FROM airport WHERE iso_country="{code}"'
    print(sql)
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(sql)
    res = cursor.fetchall()
    return res


db_connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="admin",
    autocommit=True  ##auto commits change queries to db
)

i = input("Anna maakoodi: ")
tulos = fetch_data(i)
for i in tulos:
    print(f"Nimi: {i['name']}, Tyyppi: {i['type']} ")