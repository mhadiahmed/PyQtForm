import sqlite3

db = sqlite3.connect('database')
print(' ')
db.execute('drop table if exists user')
db.execute('create table if not exists user(users text,email text, pass text);')
db.execute('insert into user(users , email, pass) values (? , ? , ?); ', ('mhadi' , 'mhadi@gmail.com','mr12345'))
db.commit()
rb = db.execute('select * from user')
for row in rb:
    print('userName: ' , row[0])
    print('Email: ' , row[1])
    print('pass: ' , row[2])