import sqlite3

#open connection
#if the db exist open
#if db not exist create then open it 
conn = sqlite3.connect('test.db')

print('connection open')

#open cursor object 
cursor = conn.cursor()

#excute tables creation in bloc try
#case table exist exception
try:
    cursor.execute('''
        CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)
    ''')
    #commit each news changes
    conn.commit()
except Exception:
    print('table exist')
print('table users created')
cursor.execute('''SELECT name, email, phone FROM users''')
user1 = cursor.fetchone() #retrieve the first row
print(user1) #Print the first column retrieved(user's name)
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

conn.close()
