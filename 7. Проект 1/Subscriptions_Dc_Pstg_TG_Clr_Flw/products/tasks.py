import os, time, telebot
from celery import shared_task
from sqlalchemy import create_engine, text

@shared_task
def send_telegram_notification(order_id):

    time.sleep(10)

    try:
        DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        engine = create_engine(DB_URL)

        with engine.connect() as conn:

            sql = text('''
                       SELECT o.id,
                              o.quantity,
                              o.total_price,
                              p.name as product_name,
                              u.telegram_id,
                              u.username
                       FROM products_order o
                                JOIN products_product p ON o.product_id = p.id
                                JOIN users_customuser u ON o.user_id = u.id
                       WHERE o.id = :order_id
                       ''')

            result = conn.execute(sql, {'order_id': order_id}).fetchone()

            if not result:
                return

            order_id_db, quantity, total_price, product_name, telegram_id, username = result

            if not telegram_id:
                return

            token = os.getenv('TELEGRAM_BOT_TOKEN')
            if not token:
                return

            bot = telebot.TeleBot(token)

            message = (
                f"Вы оформили новый заказ!\n\n"
                f"Заказ №{order_id_db}\n"
                f"Товар: {product_name}\n"
                f"Количество: {quantity}\n"
                f"Сумма: {total_price} руб.\n\n"
                f"Спасибо за покупку!"
            )

            bot.send_message(telegram_id, message)

    except Exception as e:
        print(f'Ошибка отправки уведомления: {e}')