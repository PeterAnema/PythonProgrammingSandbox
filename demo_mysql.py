
import MySQLdb as mdb
import sys

##try:
##    con = mdb.connect('localhost', 'computrain', 'computrain', 'computrain');
##
##    cur = con.cursor()
##    cur.execute("SELECT VERSION()")
##
##    ver = cur.fetchone()
##    
##    print("Database version : %s " % ver)
##    
##except e:
##  
##    print("Error %d: %s" % (e.args[0],e.args[1]))
##    sys.exit(1)
##    
##finally:    
##        
##    if con:    
##        con.close()






##con = mdb.connect('localhost', 'computrain', 'computrain', 'computrain');
##
##with con:
##    
##    cur = con.cursor()
##    cur.execute("DROP TABLE IF EXISTS Provincies")
##    cur.execute("CREATE TABLE Provincies("
##                "Id INT PRIMARY KEY AUTO_INCREMENT,"
##                "Name VARCHAR(25))")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Noord-Holland')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Utrecht')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Zuid-Holland')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Zeeland')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Noord-Brabant')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Limburg')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Gelderland')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Overijssel')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Drenthe')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Groningen')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Friesland')")
##    cur.execute("INSERT INTO Provincies(Name) VALUES('Flevoland')")


con = mdb.connect('localhost', 'computrain', 'computrain', 'computrain');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM Provincies")

    rows = cur.fetchall()

    for row in rows:
        print(row)
