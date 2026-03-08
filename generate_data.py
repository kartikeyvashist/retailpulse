import csv
import random
from faker import Faker

fake = Faker('en_IN')

# This is how we can generate customers using faker

customers = []          # Here we have created a list where our columns would be filled

for i in  range(1, 501):
    customers.append({
        'customer_id': i,
        'customer_name': fake.name(),
        'city': fake.city(),
        'email': fake.email(),
        'phone': fake.phone_number()
    })

# This is how we are going to save it to CSV

with open('data/customers.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['customer_id', 'customer_name', 'city', 'email', 'phone'])
    writer.writeheader()
    writer.writerows(customers)

print("Customers.csv created")

categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Sports']

product_names = {
    'Electronics': ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger', 'Smartwatch', 'Camera', 'Speaker', 'Keyboard', 'Mouse'],
    'Clothing': ['T-Shirts', 'Jean', 'Jacket', 'Saree', 'Kurta', 'Shorts', 'Shoes', 'Socks', 'Cap', 'Belt'],
    'Food': ['Rice', 'Dal', 'Chips', 'Biscuits', 'Chocolate', 'Coffee', 'Tea', 'Juice', 'Noodles', 'Sause'],
    'Books': ['Novals', 'Textbook', 'Comic', 'Magazine', 'Dictionary', 'Notebook', 'Diary', 'Atlas', 'Biography', 'Cookers'],
    'Sports': ['Cricket Bat', 'Football', 'Badminton Racket', 'Yoga Mat', 'Dumbbells', 'Cycle', 'Helmet', 'Gloves', 'Shoes', 'Jersey'],
}

products = []
product_id = 1

for category, items in product_names.items():       #   Here we have inserted our categories list into catagory and product name dictionary into items
    for item in items:
        products.append({
            'product_id': product_id,
            'product_name': item,
            'category': category,
            'price': round(random.uniform(50, 50000), 2)
        })
        product_id +=1

with open('data/products.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['product_id', 'product_name', 'category', 'price'])
    writer.writeheader()
    writer.writerows(products)

print("Products.csv is created")

payment_method = ['Cash', 'Credit Card', 'Debit Card', 'UPI', 'Net Banking']

orders = []

for i in range(1, 50001):
    orders.append({
        'order_id': i,
        'customer_id': random.randint(1, 500),
        'product_id': random.randint(1, 50),
        'quantity': random.randint(1, 10),
        'sale_date': fake.date_between(start_date='-2y', end_date='today'),
        'payment_method': random.choice(payment_method)
    })

with open('data/orders.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['order_id', 'customer_id', 'product_id', 'quantity', 'sale_date', 'payment_method'])
    writer.writeheader()
    writer.writerows(orders)

print("orders.csv created")