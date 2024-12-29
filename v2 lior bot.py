import telebot
from telebot import types

TOKEN = '7945760551:AAFYfbUwbTFEyYLHk2lY5R9hFuknoCtX26s'  # Updated bot token
bot = telebot.TeleBot(TOKEN)

# Start message and main buttons
@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name  # Fetch user's first name
    markup = types.ReplyKeyboardMarkup(row_width=2)
    products_btn = types.KeyboardButton("✨ Products 🛋️")
    help_btn = types.KeyboardButton("📞 Support 🌟")
    follow_us_btn = types.KeyboardButton("🌐 Social ✨")
    markup.add(products_btn, help_btn, follow_us_btn)
    bot.send_message(message.chat.id, f"Welcome, dear {user_name}! 🌟 How may we assist you today?", reply_markup=markup)

# Help button handler
@bot.message_handler(func=lambda message: message.text == "📞 Support 🌟")
def help(message):
    user_name = message.from_user.first_name  # Fetch user's first name
    bot.send_message(message.chat.id, f"Dear {user_name}, if you require any assistance, kindly contact us at 0909420082 or reach out via Telegram @Liordesign1. We are here to help. 🌟")

# Follow Us button handler
@bot.message_handler(func=lambda message: message.text == "🌐 Social ✨")
def follow_us(message):
    user_name = message.from_user.first_name  # Fetch user's first name
    markup = types.InlineKeyboardMarkup(row_width=1)
    telegram_btn = types.InlineKeyboardButton("📱 Telegram", url="https://t.me/Liordesign")
    facebook_btn = types.InlineKeyboardButton("🌍 Facebook", url="https://www.facebook.com/profile.php?id=100088499067072&mibextid=ZbWKwL")
    instagram_btn = types.InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/lior_designs_?igsh=YmpjdmN5djhxcWNr")
    tiktok_btn = types.InlineKeyboardButton("🎥 TikTok", url="https://www.tiktok.com/@lior.designs")
    markup.add(telegram_btn, facebook_btn, instagram_btn, tiktok_btn)
    bot.send_message(message.chat.id, f"Connect with us on social media, {user_name}. We look forward to hearing from you. 🌐✨", reply_markup=markup)

# Product buttons handler
@bot.message_handler(func=lambda message: message.text == "✨ Products 🛋️")
def products(message):
    user_name = message.from_user.first_name  # Fetch user's first name
    markup = types.ReplyKeyboardMarkup(row_width=2)
    lights_btn = types.KeyboardButton("💡 Lights ✨")
    shelves_btn = types.KeyboardButton("📚 Shelves 📐")
    wall_arts_sculptures_btn = types.KeyboardButton("🖼️ Wall Arts & Sculptures 🎨")
    planters_btn = types.KeyboardButton("🌿 Planters 🌸")
    back_btn = types.KeyboardButton("🔙 Back")
    markup.add(lights_btn, shelves_btn, wall_arts_sculptures_btn, planters_btn, back_btn)
    bot.send_message(message.chat.id, f"Explore our exclusive, luxurious collection of home decor, {user_name}. ✨", reply_markup=markup)

# Back button handler to go back to the main menu
@bot.message_handler(func=lambda message: message.text == "🔙 Back")
def back(message):
    user_name = message.from_user.first_name  # Fetch user's first name
    markup = types.ReplyKeyboardMarkup(row_width=2)
    products_btn = types.KeyboardButton("✨ Products 🛋️")
    help_btn = types.KeyboardButton("📞 Support 🌟")
    follow_us_btn = types.KeyboardButton("🌐 Social ✨")
    markup.add(products_btn, help_btn, follow_us_btn)
    bot.send_message(message.chat.id, f"Welcome back, {user_name}. How may we assist you today?", reply_markup=markup)

# Products: Illuminating Lights
@bot.message_handler(func=lambda message: message.text == "💡 Lights ✨")
def lights(message):
    user_name = message.from_user.first_name  # Fetch user's first name
    markup = types.ReplyKeyboardMarkup(row_width=1)
    back_btn = types.KeyboardButton("🔙 Back")
    markup.add(back_btn)
    
    # Two Lights products with images and details
    bot.send_photo(message.chat.id, "https://postimg.cc/Bjtf4pMf", caption="💡 Wall Light\nETB 1300\nCode: LIGHT-001")
    bot.send_photo(message.chat.id, "https://postimg.cc/wRJ3fHRF", caption="💡 Opulent Light\nETB 1300\nCode: LIGHT-002")
    bot.send_message(message.chat.id, f"To place an order, kindly send the product code to @Liordesign1, {user_name}. We look forward to your purchase. ✨", reply_markup=markup)

# Products: Designer Shelves
@bot.message_handler(func=lambda message: message.text == "📚 Shelves 📐")
def shelves(message):
    user_name = message.from_user.first_name  # Fetch user's first name
    markup = types.ReplyKeyboardMarkup(row_width=1)
    back_btn = types.KeyboardButton("🔙 Back")
    markup.add(back_btn)
    
    # Two Shelves products with images and details
    bot.send_photo(message.chat.id, "https://postimg.cc/VSJdVZNS", caption="📚 Dynamic Shelves\nETB 2100\nCode: SHELF-001")
    bot.send_photo(message.chat.id, "https://postimg.cc/HcGsPpKK", caption="📚 Bird Shelves\nETB 3500\nCode: SHELF-002")
    bot.send_message(message.chat.id, f"To place an order, kindly send the product code to @Liordesign1, {user_name}. We are delighted to assist you. 📐", reply_markup=markup)

# Products: Wall Arts & Sculptures
@bot.message_handler(func=lambda message: message.text == "🖼️ Wall Arts & Sculptures 🎨")
def wall_arts_sculptures(message):
    user_name = message.from_user.first_name  # Fetch user's first name
    markup = types.ReplyKeyboardMarkup(row_width=1)
    back_btn = types.KeyboardButton("🔙 Back")
    markup.add(back_btn)
    
    # Two Wall Arts & Sculptures products with images and details
    bot.send_photo(message.chat.id, "https://postimg.cc/K8mkkTm6", caption="🖼️ Abstract Sculpture\nETB 4500\nCode: SCULPT-001")
    bot.send_photo(message.chat.id, "https://postimg.cc/Rhfr73Wx", caption="🖼️ Modern Sculpture\nETB 5000\nCode: SCULPT-002")
    bot.send_message(message.chat.id, f"To place an order, kindly send the product code to @Liordesign1, {user_name}. We appreciate your interest in our products. 🎨", reply_markup=markup)

# Products: Premium Planters
@bot.message_handler(func=lambda message: message.text == "🌿 Planters 🌸")
def planters(message):
    user_name = message.from_user.first_name  # Fetch user's first name
    markup = types.ReplyKeyboardMarkup(row_width=1)
    back_btn = types.KeyboardButton("🔙 Back")
    markup.add(back_btn)
    
    # Two Planters products with images and details
    bot.send_photo(message.chat.id, "https://postimg.cc/g2L1M5YM", caption="🌿 Large Planter\nETB 1200\nCode: PLANT-001")
    bot.send_photo(message.chat.id, "https://postimg.cc/1rDPbT9W", caption="🌿 Small Planter\nETB 1000\nCode: PLANT-002")
    bot.send_message(message.chat.id, f"To place an order, kindly send the product code to @Liordesign1, {user_name}. We look forward to serving you. 🌸", reply_markup=markup)

# Running the bot
bot.polling(none_stop=True)