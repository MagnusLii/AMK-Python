
import mysql.connector

sqlconnect = mysql.connector.connect(
    host="localhost",
    port="3306",
    database="flight_game1",
    user="root",
    password="5579",
    autocommit=True
)

def sqlGetPlayers():
    sql = "SELECT id, co2_consumed, co2_budget," \
          " location, screen_name FROM game"
    print(sql)
    cursor = sqlconnect.cursor()
    cursor.execute(sql)
    outcome = cursor.fetchall()
    if cursor.rowcount > 0:
        print(outcome)
    return
