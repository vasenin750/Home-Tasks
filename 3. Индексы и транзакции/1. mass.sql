insert into orders_items (order_id, product_name, quantity, price)
select
	floor(random() * 11 + 3)::int,                       -- номер заказа из существующих (от 3 до 13)
	'Товар ' || floor(random() * 1000000 + 1)::int,      -- название товара (от 1 до 1 млн. вкл.)
	floor(random() * 10 + 1)::int,                       -- количество (от 1 до 10 вкл.)
	round((random() * (100000 - 100) + 100)::numeric, 2) -- цена (от 100 до 100 000)
from generate_series(1, 1000000) as i