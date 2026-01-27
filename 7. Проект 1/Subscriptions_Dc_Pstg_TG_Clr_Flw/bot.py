import os, telebot
from sqlalchemy import create_engine, text
import time

time.sleep(5)

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

engine = None

try:
    DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine = create_engine(DB_URL)

except Exception as e:
    print(f"Ошибка БД (продолжаем без нее): {e}")
    engine = None

@bot.message_handler(commands=['start'])
def start(message):
    user_id = int(message.from_user.id)

    bot.send_message(
        message.chat.id,
        f'Ваш ID: {user_id}\n\n'
        'Отправьте ваш номер. \n'
        'Формат: +79265655677'
    )

@bot.message_handler(func=lambda message: True)
def handle_phone(message):
    phone = message.text.strip()
    telegram_id = message.from_user.id

    if not engine:
        bot.send_message(message.chat.id, 'База данных временно недоступна')
        return

    try:
        with engine.begin() as conn:
            sql = text('''
                       SELECT id, username
                       FROM users_customuser
                       WHERE phone = :phone
                       ''')
            result = conn.execute(sql, {'phone': phone}).fetchone()

            if result:
                user_id, username = result

                update_sql = text('''
                                  UPDATE users_customuser
                                  SET telegram_id = :telegram_id
                                  WHERE id = :id
                                  ''')
                conn.execute(update_sql, {'telegram_id': telegram_id, 'id': user_id})

                bot.send_message(
                    message.chat.id,
                    f"Вы зарегистрированы.\n"
                    f"Пользователь: {username}\n"
                    f"ID: {telegram_id}"
                )
            else:
                bot.send_message(
                    message.chat.id,
                    'Пользователь с таким номером не найден.'
                )
    except Exception as e:
        print(f'Ошибка: {e}')
        bot.send_message(
            message.chat.id,
            'Ошибка. Попробуйте позже.'
        )

if __name__ == "__main__":
    bot.polling(none_stop=True)