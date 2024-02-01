import sqlite3
conn = sqlite3.connect('interviewQs/ejercicios/sources/scolarships.db')
c = conn.cursor()


scholarships = c.execute('SELECT * FROM scolarshipsAnual')
money = scholarships.fetchall()
cant_students = len(money)
for i in range(cant_students):
    money[i] = (i + 1, money[i][1] / 12)
print(money)


conn.commit()
conn.close()


#c.execute("""CREATE TABLE scolarshipsAnual(
#          id INTEGER,
#          scolarships REAL
#)""")

#estudiantes = [
#    (1, 12000),
#    (2, 18000),
#    (3, 24000),
#    (4, 15000),
#    (5, 21000),
#    (6, 13000)
#3]

#c.executemany('INSERT INTO scolarshipsAnual VALUES (?, ?)', estudiantes)