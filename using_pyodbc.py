import pyodbc as pyodbc
 
dbFile = '/Users/peter/Computrain/Python/PythonDevV3/Sandbox/AccessDatabase.mdb'

conn = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + dbFile)

#conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER= ;DATABASE=mijndatabase;UID=gebruiker;PWD=wachtwoord')

cursor = conn.cursor()
 
sql = 'SELECT * FROM klanten ORDER BY naam;'
for row in cursor.execute(sql): # cursors are iterable
    print("{}, {}".format(row.naam, row.woonplaats))
 
cursor.close()
conn.close()
