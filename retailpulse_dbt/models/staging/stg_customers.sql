SELECT
    customer_id,
    customer_name,
    city,
    email,
    phone
FROM {{ source ('retailpulse', 'customers')}}
