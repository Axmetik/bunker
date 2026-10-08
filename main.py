import os
import time

import telebot
from dotenv import load_dotenv
from telebot import types

import bunker
import messages
import person
import story
# import adding

load_dotenv()

PERSON_COOLDOWN_SECONDS = int(os.getenv('PERSON_COOLDOWN_SECONDS', 5 * 60))
last_person_request = {}


#підключення бота через унікальний токен
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise RuntimeError('BOT_TOKEN environment variable is not set')

bot = telebot.TeleBot(BOT_TOKEN)


def get_remaining_person_cooldown(user_id):
    last_request_time = last_person_request.get(user_id)
    if last_request_time is None:
        return 0

    elapsed_seconds = time.time() - last_request_time
    return max(0, int(PERSON_COOLDOWN_SECONDS - elapsed_seconds))

#Хендлер для прийому команди /start
@bot.message_handler(commands=['start'])
def start(mess):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    story_btn = types.KeyboardButton('📚Історія')
    person_btn = types.KeyboardButton('👨Персона👩')
    bunker_btn = types.KeyboardButton('☠Бункер')
    rules_btn = types.KeyboardButton('📝Правила')
    # add_btn = types.KeyboardButton('✏Відгуки')

    markup.add(person_btn, bunker_btn, story_btn, rules_btn,)

    bot.send_message(mess.chat.id, messages.start)
    bot.send_message(mess.chat.id, 'Оберіть дію', reply_markup=markup)


#Хендлер для прийому тексту(кнопки)
@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.text == '📚Історія':
        st = story.story()
        bot.send_message(message.chat.id, st.getStory())

    elif message.text == '👨Персона👩':
        remaining_seconds = get_remaining_person_cooldown(message.from_user.id)
        if remaining_seconds > 0:
            minutes = remaining_seconds // 60
            seconds = remaining_seconds % 60
            bot.send_message(
                message.chat.id,
                f'Персону можна генерувати раз на 5 хвилин. Зачекайте ще {minutes} хв {seconds} с.'
            )
            return

        last_person_request[message.from_user.id] = time.time()
        prs = person.person()
        prs.setPerson()
        bot.send_message(message.chat.id, prs.getPerson())

    elif message.text == '📝Правила':
        bot.send_message(message.chat.id, messages.rules)

    elif message.text == '☠Бункер':
        bn = bunker.bunker()
        bn.setBunker()
        bot.send_message(message.chat.id, bn.getBunker())

    elif message.text == '🔙Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        story_btn = types.KeyboardButton('📚Історія')
        person_btn = types.KeyboardButton('👨Персона👩')
        bunker_btn = types.KeyboardButton('☠Бункер')
        rules_btn = types.KeyboardButton('📝Правила')
        add_btn = types.KeyboardButton('✏Відгуки')

        markup.add(person_btn, bunker_btn, story_btn, rules_btn, add_btn)

        bot.send_message(message.chat.id, 'Оберіть дію', reply_markup=markup)

    # elif message.text == '✏Відгуки':
    #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     back_btn = types.KeyboardButton('🔙Назад')
    #     markup.add(back_btn)
    #     add_prop = bot.send_message(message.chat.id, messages.proposition, reply_markup=markup)
    #     bot.register_next_step_handler(add_prop, prop)


def prop(message):
    if message.text != '🔙Назад':
        # adding.addProp(message.text)
        bot.send_message(message.chat.id, messages.thank)
        bot.send_message(chat_id='-898448137', text=message.text)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        story_btn = types.KeyboardButton('📚Історія')
        person_btn = types.KeyboardButton('👨Персона👩')
        bunker_btn = types.KeyboardButton('☠Бункер')
        rules_btn = types.KeyboardButton('📝Правила')
        # add_btn = types.KeyboardButton('✏Відгуки')

        markup.add(person_btn, bunker_btn, story_btn, rules_btn,)

        bot.send_message(message.chat.id, 'Оберіть дію', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        story_btn = types.KeyboardButton('📚Історія')
        person_btn = types.KeyboardButton('👨Персона👩')
        bunker_btn = types.KeyboardButton('☠Бункер')
        rules_btn = types.KeyboardButton('📝Правила')
        # add_btn = types.KeyboardButton('✏Відгуки')

        markup.add(person_btn, bunker_btn, story_btn, rules_btn,)

        bot.send_message(message.chat.id, 'Оберіть дію', reply_markup=markup)

def main():
    bot.infinity_polling(skip_pending=True)


if __name__ == '__main__':
    main()
