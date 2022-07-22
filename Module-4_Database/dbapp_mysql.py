import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='tempdb')
    print("Database connected!")
except Exception as e:
    print(e)

cur=dbcon.cursor()

# Create Table
create_tbl="create table tops(id int primary key, fname text, sub text)"
try:
    cur.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
insert_data="insert into tops values(1,'Sanket','Python'),(2,'Mitesh','JAVA'),(3,'Harsh','Android'),(4,'Ashok','UIUX')"
try:
    cur.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)

# Update Data
update_data="update tops set sub='iOS' where id=3"
try:
    cur.execute(update_data )
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)

# Delete Data
delete_data="delete from tops where id=3"
try:
    cur.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)

# Select Data
select_data="select * from tops"
try:
    cur.execute(select_data)
    data=cur.fetchall()
    #print(data)
    for i in data:
        print(i[1])
except Exception as e:
    print(e)
