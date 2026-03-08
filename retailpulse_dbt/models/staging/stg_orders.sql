SELECT
    order_id,
    customer_id,
    product_id,
    quantity,
    sale_date,
    payment_method
FROM {{ source('retailpulse', 'orders')}}
