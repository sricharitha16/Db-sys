import psycopg2

# Connect to the database
conn = psycopg2.connect(host = "localhost", user = "postgres", password = "1234", database = "postgres", port = "5432")

# Query to retrieve item details by name
item_name = "Broccoli Sprouts"
cur = conn.cursor()
cur.execute("SELECT * FROM item WHERE Iname = %s", (item_name,))
rows = cur.fetchall()
print(rows)

# Query to retrieve item details by ID
item_id = 2
cur = conn.cursor()
cur.execute("SELECT * FROM ITEM WHERE iId = %s", (item_id,))
rows = cur.fetchall()
print(rows)

# Close the cursor and database connection
cur.close()
conn.close()
