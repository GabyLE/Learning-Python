import sqlite3

#make a connection to the file or created 
conn = sqlite3.connect('countorg.sqlite')
#it's like the handle when manipulating a file
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if(len(fname)<1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1].split('@')
    org = email[1]
    #dictionary part
    #it's like open a file- ? it's a place holder
    cur.execute('SELECT count FROM Counts WHERE org = ?' , (org,))
    #
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
            VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count +1 WHERE org = ?', (org,))
conn.commit() #forces everything to write on the disk

sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()