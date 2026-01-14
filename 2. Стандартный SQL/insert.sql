insert into customers (name, email)
values
('Иван Иванов', 'ivan@mail.ru'),
('Алексей Васенин', 'vaseninbox@mail.ru'),
('Алексей Кольцов', 'koltsov@mail.ru'),
('Васенина Ирина', 'irina@mail.ru')

insert into orders (customer_id)
values
(1)
(1)
(2)
(2)
(2)
(3)
(3)
(4)
(4)
(4)
(4)

insert into orders_items (order_id, product_name, quantity, price)
values
(3, 'Огурцы', 2, 120),
(3, 'Вентилятор', 1, 11500),
(4, 'Молоко', 1, 100),
(4, 'Яндекс Колонка', 1, 12000),
(5, 'Вода', 10, 120),
(6, 'Кола', 2, 90),
(6, 'Сахар', 3, 20),
(8, 'Соль', 1, 10),
(8, 'Сигареты', 1, 275),
(8, 'Зажигалка', 1, 40)






--select
select *
from customers

select *
from orders

select *
from orders_items