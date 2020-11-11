import psycopg2

#connect to the db
con = psycopg2.connect(
    host = "localhost",
    database = "dbcobacoba",
    user = "postgres",
    password = "kaumkusam25")

#cursor
cur = con.cursor()

#execute query
cur.execute("select id, name from employee")

rows = cur.fetchall()

for data in rows:
    print ("id   : " + str(data[0])) 
    print ("name : " + data[1])
    print ("")

#close the cursor
cur.close()

#close the connection
con.close()