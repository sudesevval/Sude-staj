import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
('movies',)
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
res.fetchone() is None
True
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()
res = cur.execute("SELECT score FROM movie")
res.fetchall()
[(8.2,), (7.5,)]
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit() 
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)
(1971, 'And Now for Something Completely Different')
(1975, 'Monty Python and the Holy Grail')
(1979, "Monty Python's Life of Brian")
(1982, 'Monty Python Live at the Hollywood Bowl')
(1983, "Monty Python's The Meaning of Life")
con.close()
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
