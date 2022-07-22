
import sqlite3

try:
    dbcon=sqlite3.connect("newdb.db")
    print("Database created / connected!")
except Exception as e:
    print(e)

# Table Create
create_tbl="create table studinfo(id int primary key, name text, sub text, city text)"
try:
    dbcon.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
insert_data="insert into studinfo values(1,'sanket','python','rajkot'),(2,'mitesh','java','baroda'),(3,'nirav','php','surat'),(4,'ashok','ui-ux','ahmedabad'),(5,'hitesh','android','rajkot')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted")
except Exception as e:
    print(e)

# Update Data
update_data="update studinfo set sub='iOS' where id=5"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)

# Delete Data
delete_data="delete from studinfo where id=2"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)

# Select Data(fetch)

cur=dbcon.cursor()
show_data="select * from studinfo"
try:
    cur.execute(show_data)
    data=cur.fetchall()
    #data=cur.fetchmany(3)
    #data=cur.fetchone()
    #print(data)

    for i in data:
        #print(i)
        print(i[2])
except Exception as e:
    print(e)
