# database and table creation
import sqlite3
conn = sqlite3.connect('insurance_charges.db')
cur = conn.cursor()

query_to_create_table = """
create table insurance_data(
    age int,
    sex varchar (10),
    bmi float,
    children int,
    smoker varchar (5),
    region varchar (15),
    predicted_charges float
)
"""

cur.execute(query_to_create_table)
print('YOUR DATABASE AND TABLE IS CREATED')
cur.close()
conn.close()