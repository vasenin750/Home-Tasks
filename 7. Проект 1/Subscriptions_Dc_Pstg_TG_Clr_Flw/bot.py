import os, sys, django, telebot
from sqlalchemy import create_engine, text

sys.path.append('/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(DB_URL)
bot = telebot.TeleBot(TOKEN)

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
    try:
        with engine.connect() as conn:
            sql = text('''
                       SELECT id, username 
                       FROM subscriptions_customuser 
                       WHERE phone = :phone
            ''')
            result = conn.execute(sql, {'phone': phone}).fetchone()

            if result:
                update_sql = text('''
                                  UPDATE subscriptions_customuser
                                  SET telegram_id = :telegram_id
                                  WHERE id = :id
                ''')
                conn.execute(update_sql, {'telegram_id': telegram_id, 'id': result[0]})
                conn.commit()

                bot.send_message(
                    message.chat.id,
                    f"Вы зарегистрированы.\n"
                    f"Пользователь: {result[1]}\n"
                    f"ID: {telegram_id}"
                )
            else:
                bot.send_message(
                    message.chat.id,
                    'Пользователь с таким номером не найден.'
                )
    except Exception as e:
        bot.send_message(
            message.chat.id,
            'Ошибка. Попробуйте позже.'
        )

if __name__ == "__main__":
    print('Telegram бот запущен...')
    bot.polling(none_stop=True)