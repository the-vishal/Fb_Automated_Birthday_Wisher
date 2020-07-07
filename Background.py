#Automatic Birthday wisher on facebook background version i.e
# not showing window and gui to user.
#One time set up, Paste it into Startup folder.
import re
from fbchat import Client
from fbchat.models import *
import datetime
import sqlite3
from sqlite3 import Error

now= datetime.datetime.now()
k=now.strftime("%d-%m")

db_file = "Database.db"
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def insert_birthday(birthday = ""):
    
    """ function to insert new birthdays in the database """
    conn = create_connection(db_file)
    with conn:
	    day = datetime.datetime.now()
	    day = now.strftime("%d-%m")
	    names = "Testname"
	    birthday = (names, day)
	    sql = ''' INSERT INTO birthdays(name, birthday)VALUES(?,?)'''
	    cur = conn.cursor()
	    cur.execute(sql, birthday)
	    return cur.lastrowid


def select_name(date=k):

    """Get name for the date given"""
    conn = create_connection(db_file)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM birthdays WHERE birthday=?",(date,))
        rows = cur.fetchall()

    for row in rows:
        print(row[0])
    return rows

cont = select_name(k)


if k in cont:
    patt1=r"([\w]+) ([\w]+):"+k
    mat=re.search(patt1,cont)
    #print(mat.group())
    patt=r"([\w]+) ([\w]+)"
    match = re.search(patt,mat.group())
    if match:
     #print(match.group())
     name=match.group()
     #print("Match Found")
     client = Client('USERNAME', 'PASSWORD')
     users = client.searchForUsers(name)
     user = users[0]
     #print("User's ID: {}".format(user.uid))
     # client.sendMessage('Happy Birthday '+name,thread_id=user.uid,thread_type=ThreadType.USER)
     client.sendLocalImage("cake.jpg", 'Happy Birthday' + name, thread_id=user.uid, thread_type=ThreadType.USER)
     #print("Message sent")
    else:
        pass





