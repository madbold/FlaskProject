import sqlite3

connection=sqlite3.connect("Test.db")
cursor=connection.cursor()
create_table= "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username Text ,password Text)"
create_item_table="CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY , name Text , price int)"
cursor.execute(create_table)

cursor.execute(create_item_table) # creating item table

user=(1,"amit","asdf")
item=("table",160)
insert_data="INSERT  INTO user VALUES(?,?,?)"
insert_item="INSERT  INTO items VALUES(NULL,?,?)"

cursor.execute(insert_data,user) #insert one row
cursor.execute(insert_item,item) #insert one row

users=[
        (2,"vinod","1234"),
        (3,"sachin","wert")
]

cursor.executemany(insert_data,users) #insert many rows

connection.commit()
fetch_data="SELECT * from items"
for row in cursor.execute(fetch_data):
    print(row)


connection.close()
