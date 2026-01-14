select o.id, o.order_date, c.name
from orders o
join customers c on o.customer_id = c.id

select product_name, quantity, price
from orders_items
where order_id = 3
order by price desc

select c.name, sum(oi.price * oi.quantity) as total_spent
from orders_items oi
join orders o on oi.order_id = o.id
join customers c on o.customer_id = c.id
group by c.name
having sum(oi.price * oi.quantity) > 5000








/* 
--Проверка
select *
from orders_items oi
join orders o on oi.order_id = o.id
join customers c on o.customer_id = c.id 
*/