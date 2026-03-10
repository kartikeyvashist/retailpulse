SELECT
    c.customer_name,
    c.city,
    p.product_name,
    p.category,
    o.quantity, 
    p.price,
    round((o.quantity * p.price):: numeric) AS revenue,
    o.sale_date,
    o.payment_method

FROM {{ref('stg_orders')}} o
JOIN {{ref('stg_products')}} p ON o.product_id = p.product_id
JOIN {{ref('stg_customers')}} c ON o.customer_id = c.customer_id
