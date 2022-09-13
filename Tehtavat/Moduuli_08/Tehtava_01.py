
import SQLfunctions


def getICAOinf(icao):
    sql = f'''SELECT name, municipality
      FROM airport
      WHERE ident = "{icao}"'''
    #print(sql)
    cursor = SQLfunctions.sqlconnect.cursor()
    cursor.execute(sql)
    outcome = cursor.fetchall()
    return outcome


print(getICAOinf(input("Anna ICAO: ".upper())))
