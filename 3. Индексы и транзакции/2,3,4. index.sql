create index orders_customer_id_idx on orders(customer_id)
create index comp_order_items_idx on orders_items(order_id, price)
create index product_name_order_items_idx on orders_items(product_name)

explain analyze 
select * 
from orders_items
where price > 10000 and order_id = 123

"Index Scan using comp_order_items_idx on orders_items  (cost=0.42..8.43 rows=1 width=37) (actual time=0.030..0.030 rows=0.00 loops=1)"

explain analyze 
select * 
from orders
where customer_id = 1

"Seq Scan on orders  (cost=0.00..1.14 rows=1 width=16) (actual time=0.024..0.026 rows=2.00 loops=1)"

drop index orders_customer_id_idx
Индекс по полю customer_id в таблице orders удален, потому что он не используется.
А не исользуется он видимо потому, что в базе всего 4 покупателя создано (небольшой массив данных, низкая селективность).