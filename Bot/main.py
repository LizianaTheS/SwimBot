from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from . import bot


@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()

    btn_home = InlineKeyboardButton("🏠 صفحه اصلی سایت", url="https://irswim.ir/")
    btn_topic1 = InlineKeyboardButton("📘 مقالات آموزشی", url="https://irswim.ir/category/آموزش-شنا/")
    btn_swim_types = InlineKeyboardButton("🏊 انواع شنا", callback_data="swim_types")

    markup.add(btn_swim_types)
    markup.add(btn_home)

    bot.send_message(message.chat.id, "🏊‍♂️ سلام! یکی از گزینه‌ها رو انتخاب کن:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "swim_types")
def show_swim_topics(call):
    markup = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton("🐬 کرال سینه", callback_data="freestyle")
    btn2 = InlineKeyboardButton("🏊 کرال پشت", callback_data="backstroke")
    btn3 = InlineKeyboardButton("🐸 قورباغه", callback_data="breaststroke")
    btn4 = InlineKeyboardButton("🦋 پروانه", callback_data="butterfly")
    btn5 = InlineKeyboardButton("💪 شنای استقامتی", callback_data="endurance")
    btn6 = InlineKeyboardButton("🤿 غواصی", callback_data="diving")

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5, btn6)

    bot.send_message(call.message.chat.id, "یکی از سبک‌های شنا رو انتخاب کن:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "freestyle")
def send_freestyle_link(call):
    bot.send_message(call.message.chat.id, "🔗 لینک آموزش کرال سینه:\nhttps://irswim.ir/")

@bot.callback_query_handler(func=lambda call: call.data == "backstroke")
def send_backstroke_link(call):
    bot.send_message(call.message.chat.id, "🔗 لینک آموزش کرال پشت:\nhttps://irswim.ir/")

@bot.callback_query_handler(func=lambda call: call.data == "breaststroke")
def send_breaststroke_link(call):
    bot.send_message(call.message.chat.id, "🔗 لینک آموزش قورباغه:\nhttps://irswim.ir/")

@bot.callback_query_handler(func=lambda call: call.data == "butterfly")
def send_butterfly_link(call):
    bot.send_message(call.message.chat.id, "🔗 لینک آموزش پروانه:\nhttps://irswim.ir/")

@bot.callback_query_handler(func=lambda call: call.data == "endurance")
def send_endurance_link(call):
    bot.send_message(call.message.chat.id, "🔗 لینک تمرین‌های استقامتی:\nhttps://irswim.ir/")

@bot.callback_query_handler(func=lambda call: call.data == "diving")
def send_diving_link(call):
    bot.send_message(call.message.chat.id, "🔗 لینک آموزش غواصی:\nhttps://irswim.ir/")


@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "🏊‍♂️ **راهنمای ربات خانه شنا**\n\n"
        "این ربات برای کمک به شما در یادگیری و دسترسی سریع به موضوعات مختلف شنا طراحی شده.\n\n"
        "**دستورات و گزینه‌ها:**\n"
        "/start - شروع ربات و مشاهده منوی اصلی\n"
        "/help - مشاهده همین راهنما\n\n"
        "**دکمه‌ها:**\n"
        "🏠 صفحه اصلی سایت - برای رفتن به سایت خانه شنا\n"
        "🏊 انواع شنا - مشاهده سبک‌های مختلف شنا و لینک هر سبک\n"
        "📘 مقالات آموزشی - آموزش‌های عمومی و مقالات\n"
        "📍 آدرس استخرها - معرفی و دسترسی به استخرها\n"
        "🏆 مسابقات و قوانین - اطلاعات مسابقات و قوانین\n\n"
        "برای شروع، از /start استفاده کنید و یا یکی از دکمه‌ها را انتخاب کنید."
    )

    bot.send_message(message.chat.id, help_text)
