import sqlite3
conn = sqlite3.connect('insurance_charges.db')
cur = conn.cursor()

query = 'select * from insurance_data;'
cur.execute(query)

for record in cur.fetchall():
    print(record)

cur.close()
conn.close()