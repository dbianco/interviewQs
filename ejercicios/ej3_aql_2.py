import sqlite3
conn = sqlite3.connect('interviewQs/ejercicios/sources/availableItems.db')
c = conn.cursor()

available_items = c.execute('SELECT *, COUNT(*) total FROM availableitems GROUP BY item_name, item_type ORDER BY item_type')
result = available_items.fetchall()
print(result)

conn.commit()
conn.close()




#items = [
#    (1, 'SafeDisk 4GB', 'USB drive'),
#    (2, 'SafeDisk 8GB', 'USB drive'),
#    (3, 'Cinco 50-Pack', 'DVD'),
#    (4, 'SafeDisk 4GB', 'Memory card'),
#    (5, 'SafeDisk 8GB', 'Memory card'),
#    (6, 'Cinco 30-Pack', 'DVD'),
#    (7, 'SafeDisk 4GB', 'Memory card'),
#    (8, 'SafeDisk 4GB', 'Memory card'),
#    (9, 'DiskHolder', 'Misc'),
#    (10, 'Cinco 50-Pack', 'DVD'),
#    (11, 'SafeDisk 4GB', 'USB drive'),
#    (12, 'DiskCleaner Pro', 'Misc')
#]
#c.executemany('INSERT INTO availableItems VALUES (?, ?, ?)', items)

#c.execute("""CREATE TABLE availableItems(
#          id INTEGER,
#          item_name TEXT,
#          item_type TEXT
#)""")