'''
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan
kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
'''

import mysql.connector

def fetch_data(icao):
    sql = f'SELECT name, municipality FROM airport WHERE ident="{icao}"'
    print(sql)
    cursor = db_connection.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
    return res


#connection
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    database="flight_game",
    user="root",
    password="admin",
    autocommit=True  ##auto commits change queries to db
)

icao = input("Anna ICAO-koodi: ")
fetch_data(icao)
print()


