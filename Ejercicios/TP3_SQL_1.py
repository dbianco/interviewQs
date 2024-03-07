import sqlite3
conn= sqlite3.connect('interviewQs/Ejercicios/sources/scholarship.db')
c = conn.cursor()


# c.execute("""CREATE TABLE scholarships (
#           id int,
#           scholarship int
# )""")

# students = [
#     (1,12000),
#     (2,18000),
#     (3,24000),
#     (4,15000),
#     (5,21000),
#     (6,13000)
# ]

# c.executemany("INSERT INTO scholarships VALUES (?,?)", students)


# c.execute("SELECT * FROM scholarships")

# resultados = c.fetchall()

# for fila in resultados:
#     print(fila)

c.execute ('SELECT id, scholarship / 12 AS scholarship FROM scholarships ORDER BY id')

results  = c.fetchall()

for row in results:
    print(row)
# conn.commit()
conn.close()