import sqlite3
import pandas as pd

connection = sqlite3.connect("database.sqlite")

drop_query = "DROP TABLE IF EXISTS temp_data;"
create_query = "CREATE TABLE temp_data ( \
                  date INTEGER, \
                  city VARCHAR(80), \
                  temperature REAL, \
                  destination INTEGER);"

connection.execute(drop_query)
connection.execute(create_query)

connection.commit()

data = [(20190910, "Rome",   80.0, 0),
        (20190910, "Berlin", 50.0, 0),
        (20190910, "Wien",   32.0, 1),
        (20190911, "Paris",  65.0, 0)]

insert_query = "INSERT INTO temp_data VALUES(?, ?, ?, ?)"

connection.executemany(insert_query, data)
connection.commit()

selection_query = "SELECT date, city, temperature, destination \
                   FROM temp_data WHERE Date >= 20190101"

retrieved = pd.read_sql_query(selection_query, connection)
print(retrieved)

