import mysql.connector

def add_bark(sql_values):
  mydb = mysql.connector.connect(
    host="localhost",
    user="koira",
    passwd="koira",
    database="homestead" 
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO barks (id, bark, sector) VALUES (1, %s, %s)"
  val = sql_values
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")