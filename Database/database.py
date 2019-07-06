import sqlite3

#create
conn=sqlite3.connect('trial.db')
print('created')

register_query=str("CREATE TABLE IF NOT EXISTS register(id INTEGER PRIMARY KEY,"+
                     "username VARCHAR,"+
                     "age INTEGER,"+
                     "address VARCHAR,"+
                     "mobile INTEGER)")
                     
conn.execute(register_query)
print("created register table")
conn.close()
    
#inputs
Id=int(input('enter the id'))
Name=input('enter the name')
Age=int(input('enter the age'))
Address=input('enter the add')
Mobile=int(input('enter the contact no'))

#inserting

conn=sqlite3.connect('trial.db')

Insert_query=str("INSERT INTO register (id,username,age,address,mobile) VALUES(?,?,?,?,?)")
conn.execute(Insert_query,(Id,Name,Age,Address,Mobile))
conn.commit()
