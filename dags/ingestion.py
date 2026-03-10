import csv
import psycopg2
import os

conn = psycopg2.connect(
    host=os.environ.get('DB_HOST', 'retailpulse-db'),
    database="retailpulse",
    user="admin",
    password="admin123",
    port="5432"
)

cursor = conn.cursor()

with open('/opt/airflow/dags/data/customers.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO customers (customer_id, customer_name, city, email, phone)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING          
""", (row['customer_id'], row['customer_name'], row['city'], row['email'], row['phone']))
        
print("Customers inserted!")

with open('/opt/airflow/dags/data/products.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO products (product_id, product_name, category, price)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING          
""", (row['product_id'], row['product_name'], row['category'], row['price']))

print("Products inserted")

with open('/opt/airflow/dags/data/orders.csv', 'r', encoding='utf-8', errors='ignore') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO orders (order_id, customer_id, product_id, quantity, sale_date, payment_method)
            VALUES (%s,%s,%s,%s,%s,%s)
            ON CONFLICT DO NOTHING          
""", (row['order_id'], row['customer_id'], row['product_id'], row['quantity'], row['sale_date'], row['payment_method']))

print("Orders inserted")

conn.commit()
conn.close()
