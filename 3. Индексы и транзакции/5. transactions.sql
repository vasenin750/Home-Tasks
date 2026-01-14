do $$
declare 
	new_order_id integer;
begin
	insert into orders (customer_id)
	values (4)
	returning id into new_order_id;

	insert into orders_items (order_id, product_name, quantity, price)
	select 
		new_order_id,
		'Товар_' || i,
		floor(random() * 20 + 1)::int,
		round((random() * (10000 - 100) + 100)::numeric, 2)
	from generate_series(1, 5) as i;

	raise notice 'Успешно! ID: %', new_order_id;
	
exception when others then
	raise exception 'Ошибка: %', SQLERRM;
end $$