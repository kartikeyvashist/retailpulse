# RetailPulse 🚀
A production-grade ELT pipeline for retail analytics.

## Stack
- Python
- PostgreSQL
- Docker

## About
RetailPulse is a production-grade ELT pipeline that handles customer, product and order data. 
It ingests and processes 50,000+ records across 3 normalized tables using Python, PostgreSQL and Docker.

## Stack

- Python
- PostgreSQL
- Docker
- Faker (data generation)
- psycopg2 (database connection)

## Project Structure
- `docker-compose.yml` - In this file we have created our environment for our database where we gave name to our database, container and set-up our Username and password for postgreSQl
- `db.py` - In this file we connected our database to python using psycopg2 and created our 3 tables customers, products, orders.
- `generate_data.py` - In this file we generated fake data for those tables faker library and combine that data into seperate CSV files using file system and CSV library and saved it into our folder
- `ingestion.py` - In this file we took those CSV files and inserted into tables using psycopg2 
## How to run
1. Clone the repo
2. Run `docker compose up -d`
3. Run `python db.py`

## Database Schema

### customers
| Column | Type |
|--------|------|
| customer_id | INT (PK) |
| customer_name | VARCHAR |
| city | VARCHAR |
| email | VARCHAR |
| phone | VARCHAR |

### products
| Column | Type |
|--------|------|
| product_id | INT (PK) |
| product_name | VARCHAR |
| category | VARCHAR |
| price | FLOAT |

### orders
| Column | Type |
|--------|------|
| order_id | INT (PK) |
| customer_id | INT (FK) |
| product_id | INT (FK) |
| quantity | INT |
| sale_date | DATE |
| payment_method | VARCHAR |

## Dashboard
Live analytics dashboard built with Metabase showing:
- Revenue by Category
- Top 10 Customers by Spending
- Most Popular Payment Methods
- Cities Needing Attention
- Monthly Revenue Trend

## Running the Full Stack
1. `docker compose up -d` - starts Postgres and Metabase
2. `python db.py` - creates tables
3. `python generate_data.py` - generates 50,550 rows of fake data
4. `python ingestion.py` - loads data into Postgres
5. Open `http://localhost:3000` - view Metabase dashboard

