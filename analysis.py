import psycopg2
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

engine = create_engine('postgresql://admin:admin123@127.0.0.1:5432/retailpulse')


conn = psycopg2.connect(
    host=os.environ.get('DB_HOST', 'retailpulse-db'),
    database=os.environ.get('DB_NAME', 'retailpulse'),
    user=os.environ.get('DB_USER', 'admin'),
    password=os.environ.get('DB_PASSWORD', 'admin123'),
    port=os.environ.get('DB_PORT', '5432')
)

cursor = conn.cursor()

query = """
    SELECT round(SUM(o.quantity * p.price):: numeric, 2) AS total_revenue
    FROM orders o
    JOIN products p ON o.order_id = p.product_id

"""
df = pd.read_sql(query, engine)
print("Total Revenue: ")
print(df)
print()

query2 = """
    SELECT p.product_name, SUM(o.quantity) AS total_quantity
    FROM orders o
    JOIN products p ON p.product_id = o.order_id 
    GROUP BY p.product_name
    ORDER BY total_quantity DESC
    LIMIT 5
"""
df2 = pd.read_sql(query2, engine)
print("Top 5 Products by Quantity Sold: ")
print(df2)
print()

query3 = """
    SELECT payment_method, count(*) as total_transaction
    FROM orders
    GROUP BY payment_method
    ORDER BY total_transaction DESC
"""

df3 = pd.read_sql(query3, engine)
print("Most Popular Transaction Methods: ")
print(df3)
print()

query4 = """
    SELECT p.category, round(SUM(o.quantity * p.price):: numeric, 2) AS revenue
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.category
    ORDER BY revenue DESC
    LIMIT 3
"""

df4 = pd.read_sql(query4, engine)
pd.options.display.float_format = '{:,.2f}'.format
print("Top 3 Categories by Revenue: ")
print(df4)
print()

query5 = """
    SELECT c.city, round(SUM(o.quantity * p.price)) AS revenue
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN products p ON o.product_id = p.product_id
    GROUP BY c.city
    ORDER BY revenue ASC
    LIMIT 5
"""

df5 = pd.read_sql(query5, engine)
print("Bottom 5 Citites by Revenue: ")
print(df5)
print()

query6 = """
    SELECT c.customer_name, round(SUM(o.quantity * p.price)) AS Spendings
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN products p ON o.product_id = p.product_id
    GROUP BY c.customer_name
    ORDER BY Spendings DESC
    LIMIT 10
"""
df6 = pd.read_sql(query6, engine)
print("Top 10 Customers by Spending: ")
print(df6)
print()