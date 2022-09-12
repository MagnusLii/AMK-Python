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
