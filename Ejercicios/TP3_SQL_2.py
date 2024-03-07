import sqlite3
conn = sqlite3.connect('interviewQs\Ejercicios\sources\suspects.db')
c = conn.cursor()

# c.execute ('''CREATE TABLE Suspect (
#         id int,
#         name varchar (255),
#         surname varchar (255),
#         height float,
#         weight float
# )''')

# conn.commit()
# conn.close()


# suspects= [
#     (1,'John','Doe',165,60),
#     (2,'Bill','Green',170,67),
#     (3,'Baelfire','Grehn',172,70),
#     (4,'Bill','Gretan',185,55),
#     (5,'Brendon','Grewn',180,50),
#     (6,'bill','Green',172,50)
# ]

# c.executemany ('INSERT INTO Suspect VALUES (?,?,?,?,?)', suspects)

# c.execute('SELECT * FROM suspect')

# results = c.fetchall()
# for rows in results:
#     print(rows)

c.execute('''SELECT id, name, surname FROM suspect WHERE NOT (name  LIKE 'B%' AND surname  LIKE 'Gre_n' AND height >170) ''')

results = c.fetchall()
for rows in results:
    print(rows)


conn.close()