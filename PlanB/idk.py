import datetime as dt
import sqlite3 as sql

conn = sql.connect('final.db')  #add file location later
curs = conn.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS Users
             (id INTEGER PRIMARY KEY,
             username TEXT NOT NULL,
             email TEXT NOT NULL)
            """)

curs.execute("""CREATE TABLE IF NOT EXISTS Events 
             (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             creator TEXT NOT NULL,
             begins DATETIME NOT NULL,
             ends DATETIME NOT NULL,
             location TEXT NOT NULL,
             details TEXT 
             )""")

curs.execute("""CREATE TABLE IF NOT EXISTS Attendants
             (id INTEGER PRIMARY KEY,
             event TEXT NOT NULL,
             buyer TEXT NOT NULL,
             buyer_email TEXT NOT NULL, 
             FOREIGN KEY (event) REFERENCES Events (name)
             )""")

conn.commit()

def timeinput(v):
    while 1:
        data = input(f'{v} date and time (in YYYY-MM-DD hh:mm:ss format): ')
        try:
            dt.datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
            return data
        except ValueError:
            print('incorrect format, pls reenter the date and time.')

def create_event(username):
    name = input('Name of the event: ')
    begins = timeinput('Beginning')
    ends = timeinput('Ending')
    location = input('Locatin of the event: ')
    details = input('Details of the event: ')
    creator = username
  
    curs.execute('''
                 INSERT INTO Events (name, creator, begins, ends, location, details) 
                 VALUES (?, ?, ?, ?, ?, ?)
                ''', (name, creator, begins, ends, location, details))
    conn.commit()
    print('Event Created successfuly!')

def edit_event(name):
    selev = input('please enter the id of the event you wish to cahnge')
    selcol= input('''which column?
             1. name
             2. beginning time 
             3. ending time
             4. location
             5. desc
             6. delete event
             ''')
    newval= input('enter new values(leave blank if you are deleting): ')

    selcol = int(selcol)

    if selcol == 1:
        curs.execute('UPDATE Events SET name = ? WHERE id = ? AND creator = ?;', (newval, selev, name))
        conn.commit()
    elif selcol == 2:
        if timeinput('New beginning'):
            curs.execute('UPDATE Events SET begins = ? WHERE id = ? AND creator = ?;', (newval, selev, name))
            conn.commit()
    elif selcol == 3:
            if timeinput('New ending'):
                curs.execute('UPDATE Events SET ends = ? WHERE id = ? AND creator = ?;', (newval, selev, name))
                conn.commit()
    elif selcol == 4:
        curs.execute('UPDATE Events SET location = ? WHERE id = ? AND creator = ?;', (newval, selev, name))
        conn.commit()
    elif selcol == 5:
        curs.execute('UPDATE Events SET details = ? WHERE id = ? AND creator = ?;', (newval, selev, name))
        conn.commit()
    elif selcol == 6:
        curs.execute('DELETE FROM Events WHERE id = ? AND creator = ?', (selev, name))
        conn.commit()
    else:
        print('invalid input')

def buy_tickets(un, email):
    ev = input('Which event would you like to attend?\n')
    curs.execute('INSERT INTO Attendants (event, buyer, buyer_email) VALUES (?, ?, ?)', (ev, un, email))
    conn.commit()

def checkEvents():
    curs.execute('SELECT * FROM Events')
    rows = curs.fetchall()

    for row in rows:
        print(row)

def checkAttendants():
    ie = input("Which event's attendans do you wish to view?\n")
    curs.execute('SELECT * FROM Attendants WHERE event = (?)', (ie, ))
    rows = curs.fetchall()

    for row in rows:
        print(row)

def is_user(username, email):
    curs.execute('SELECT COUNT(*) FROM Users WHERE username = ? AND email = ?', (username, email))
    result = curs.fetchone()[0]
    if result > 0:
        return True
    else:
        while 1:
            choice = input('User not found. add user?[y/n]: ')
            if choice == 'y':
                curs.execute('INSERT INTO Users (username, email) VALUES (?, ?)', (username, email))
                conn.commit()
                return True
            elif choice == 'n':
                return False
            else:
                print('wrong input')

run=1
iusername = input('Username: ')
iemail = input('Email: ')
if is_user(iusername, iemail):
    while run:
        select= input("""
            Choose Action:
            1. Create event
            2. Edit event
            3. Buy tickets to other events
            4. Check all events
            5. Check atttendants of an event
            6. quit
            """)
        select = int(select)
        if select == 1:
            create_event(iusername)
        elif select == 2:
            edit_event(iusername)
        elif select == 3:
            buy_tickets(iusername, iemail)
        elif select == 4:
            checkEvents()
        elif select == 5:
            checkAttendants()
        elif select == 6:
            curs.close()
            conn.close()
            run= False
        else:
            print('invalid input')