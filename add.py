import sqlite3
import os
c=0

db = sqlite3.connect('requests/dtbs/db.db')
db.row_factory = sqlite3.Row
# create db and import data
try:
    db.execute('create table auto_login_sut (username text, password text)')
except:
    print('ok')
while True:
    usr = input("Enter Username:\n")
    psw = input("Enter Password:\n")

    db.execute('insert into auto_login_sut (username,password) values ("{}","{}")'.format(usr,psw))
    db.commit()
    input('Done!')

    os.system("cls")
