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
    CREATE TABLE IF NOT EXISTS customers(
        customer_id SERIAL PRIMARY KEY,
        customer_name VARCHAR(50),
        city VARCHAR(50),
        email VARCHAR(50),
        phone VARCHAR(50)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(100),
        category VARCHAR(50),
        price FLOAT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        product_id INTEGER REFERENCES products(product_id),
        customer_id INTEGER REFERENCES customers(customer_id),
        order_id SERIAL PRIMARY KEY,
        sale_date DATE,
        quantity INTEGER,
        payment_method VARCHAR(50)
    )
""")


conn.commit()
conn.close()

print("Done")