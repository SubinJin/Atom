import sqlite3

conn = sqlite3.connect('emaildb.sqlite') # eamildb.sqlite가 없어도 알아서 생성되서 저장됨
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter file name : ')
if(len(fname) < 1) :
    fname = 'mbox-short.txt'
# 파일명이 없으면 mbox-short로
fh = open(fname)

for line in fh :
    if not line.startswith('From: ') :
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email, ))
    row = cur.fetchone() # 한개의 data 조회
    if row is None :
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email, ))
    else :
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email, ))
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr) :
    print(str(row[0]), row[1])

cur.close()
