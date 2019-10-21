import mysql.connector
from mysql.connector import errorcode

try:
    conn = mysql.connector.connect(host='localhost',
                                   user='gebruiker', password='wachtwoord',
                                   database='mijndatabase')

    cursor = conn.cursor()

#    statement = ("INSERT INTO klanten "
#                 "(naam, adres, woonplaats, leeftijd) "
#                 "VALUES (%s, %s, %s, %s)")
#
#    cursor.execute(statement, ("Peter", "", "Amsterdam", 58))
#
#    conn.commit()

    query = ("SELECT naam, adres, woonplaats, leeftijd "
             "FROM klanten "
             "WHERE woonplaats LIKE %s")
    
    cursor.execute(query, ("A%",))
    
    for (naam, adres, woonplaats, leeftijd) in cursor:
        print("{}: {}, {}".format(naam, adres, woonplaats))
    
    cursor.close()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists")
    else:
        print(err)

else:
    conn.close()


#c=db.cursor()
#
#c.execute("""SELECT * FROM klanten""")
#
#print(c.rowcount)
#
#results=c.fetchall()
#print(results)
