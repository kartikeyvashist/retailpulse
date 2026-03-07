import psycopg2

#   Here we have created a connection for our database
conn = psycopg2.connect(
    host="127.0.0.1",
    database="retailpulse",
    user="admin",
    password="admin123",
    port="5432"
)

cursor = conn.cursor()

#   Here we have created a table using SQL 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales(
        id SERIAL PRIMARY KEY,
        product_name VARCHAR(100),
        sale_date DATE,
        quantity INTEGER,
        price FLOAT
    )
""")

conn.commit()
conn.close()

print("Done")