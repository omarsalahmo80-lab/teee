import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import random
import pandas as pd
from datetime import datetime, timedelta


TOKEN = '8959443016:AAFOQ7o1z7f9f2CmBOJAQiOldqwNDqNhbUM'
bot = telebot.TeleBot(TOKEN)

APPROVED_EMAILS = ['Kiser']
VALID_LICENSE_KEY = 'Kiser'
LICENSE_EXPIRY_DATE = '2030-12-12'


QUOTEX_OTC_PAIR = ['USDINR-OTCq', 'USDBDT-OTCq', 'BRLUSD-OTCq', 'USDPKR-OTCq', 'USDTRY-OTCq', 'USDMXN-OTCq', 'USDARS-OTCq', 'USDDZD-OTCq', 'USDEGP-OTCq', 'USDNGN-OTCq', 'USDCOP-OTCq', 'USDIDR-OTCq', 'USDJPY-OTCq', 'USDPHP-OTCq', 'USDCHF-OTCq', 'USDCAD-OTCq', 'NZDCAD-OTCq', 'NZDCHF-OTCq', 'NZDUSD-OTCq', 'CADCHF-OTCq', 'GOLD  -OTCq', 'FB    -OTCq', 'MSFT  -OTCq', 'INTEL -OTCq', 'MCD   -OTCq', 'EURSEK-OTCq', 'GBPNZD-OTCq', 'NZDJPY-OTCq', 'GBPJPY-OTCq', 'AUDNZD-OTCq', 'CADJPY-OTCq', 'NZDCHF-OTCq', 'USDBRL-OTCq', 'USDTRY-OTCq', 'AUDNZD-OTCq', 'CADJPY-OTCq', 'USDDZD-OTCq', 'USDBDT-OTCq', 'NZDUSD-OTCq', 'EURUSD-OTCq', 'AVAX  -OTCq', 'BEAM  -OTCq', 'BNB   -OTCq', 'BONK  -OTCq', 'BTC   -OTCq', 'DOGE  -OTCq', 'DOT   -OTCq', 'ETH   -OTCq', 'GALA  -OTCq', 'HAMSTR-OTCq']
BINOLLA_OTC_PAIR = ['AUDCHF-OTCb', 'AUDJPY-OTCb', 'AUDUSD-OTCb', 'EURAUD-OTCb', 'EURCAD-OTCb', 'EURGBP-OTCb', 'EURJPY-OTCb', 'EURUSD-OTCb', 'GBPAUD-OTCb', 'GBPCAD-OTCb', 'GBPCHF-OTCb', 'GBPUSD-OTCb', 'USDBDT-OTCb', 'USDBRL-OTCb', 'USDCAD-OTCb', 'USDCHF-OTCb', 'USDINR-OTCb', 'USDPKR-OTCb', 'NZDUSD-OTCb']
POCKET_OTC_PAIR = ['APL   -OTCp', 'AXP   -OTCp', 'FB    -OTCp', 'PFZR  -OTCp', 'TESLA -OTCp', 'AEDCNY-OTCp', 'ETC   -OTCp', 'BTC   -OTCp', 'ALB   -OTCp', 'NTFX  -OTCp', 'GODCNY-OTCp', 'SARCNY-OTCp', 'USDBDT-OTCp', 'USDBRL-OTCp', 'USDIDR-OTCp', 'USDINR-OTCp', 'USDMXN-OTCp', 'USDRUB-OTCp', 'JNJ   -OTCp', 'EURTRY-OTCp', 'USDCHN-OTCp', 'USDMYR-OTCp', 'USDTHB-OTCp', 'SILVER-OTCp', 'GOLD  -OTCp', 'MCD   -OTCp', 'MSFT  -OTCp', 'USDDZD-OTCp', 'INTEL -OTCp', 'QARCNY-OTCp', 'AUS200-OTCp', 'CAC40 -OTCp', 'D30EUR-OTCp', 'E35EUR-OTCp', 'E50EUR-OTCp', 'F40EUR-OTCp', 'US100 -OTCp', 'SMI20 -OTCp', 'SP500 -OTCp', 'JPN225-OTCp', 'USDARS-OTCp', 'USDCOP-OTCp', 'USDJPY-OTCp', 'USDPKR-OTCp', 'USDPHP-OTCp', 'USDDZD-OTCp', 'USDEGP-OTCp', 'USDNGN-OTCp', 'USDVND-OTCp', 'USDCHF-OTCp']
REAL_MARKET_PAIR = ['EUR/GBP', 'EUR/USD', 'USD/CAD', 'USD/JPY', 'EUR/JPY', 'EUR/CAD', 'GBP/AUD', 'CAD/JPY', 'AUD/JPY', 'AUD/CAD', 'AUD/USD', 'GBP/USD', 'GBP/CHF', 'USD/CHF']

user_data = {}
authenticated_users = set()


def generate_signals(selected_assets, total_signals, trading_direction, strategy):
    current_time = datetime.now()
    time_gaps = {'1': 3, '2': 4, '3': 6, '4': random.choice([5, 10, 15]), '5': 8, '6': random.choice([3, 4, 5, 6, 8])}
    time_gap = time_gaps.get(strategy, 5)
    
    minutes = current_time.minute
    remainder = minutes % time_gap
    if remainder != 0:
        current_time = current_time.replace(minute=minutes - remainder)
        
    signals = []
    for i in range(total_signals):
        asset = random.choice(selected_assets)
        if trading_direction == '1':
            direction = 'CALL'
        elif trading_direction == '2':
            direction = 'PUT'
        else:
            direction = random.choice(['CALL', 'PUT'])
            
        if strategy == '6':
            time_gap = random.choice([3, 4, 5, 6, 8])
        elif strategy == '4':
            time_gap = random.choice([5, 10, 15])
            
        signal_time = current_time + timedelta(minutes=time_gap)
        time_str = signal_time.strftime('%H:%M')
        signals.append({'Asset': asset.strip(), 'Time': time_str, 'Direction': direction})
        current_time = signal_time
        
    df = pd.DataFrame(signals)[['Asset', 'Time', 'Direction']]
    return df



@bot.message_handler(commands=['start'])
def start_bot(message):
    chat_id = message.chat.id
    if chat_id in authenticated_users:
        ask_broker(message)
    else:
        bot.send_message(chat_id, "✦ Kiser OTC - SIGNALS GENERATOR ✦\n\nLogin Required.\nPlease enter your **Email**:", parse_mode='Markdown', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, check_email)

def check_email(message):
    chat_id = message.chat.id
    email = message.text.strip()
    if email in APPROVED_EMAILS:
        bot.send_message(chat_id, "Please enter your **License Key**:", parse_mode='Markdown')
        bot.register_next_step_handler(message, check_license)
    else:
        bot.send_message(chat_id, "❌ Invalid email. Access denied. /start")

def check_license(message):
    chat_id = message.chat.id
    key = message.text.strip()
    current_date = datetime.now().strftime('%Y-%m-%d')
    if key == VALID_LICENSE_KEY and current_date <= LICENSE_EXPIRY_DATE:
        authenticated_users.add(chat_id)
        bot.send_message(chat_id, "✅ License validated. Welcome!")
        ask_broker(message)
    else:
        bot.send_message(chat_id, "❌ Invalid or expired license key. /start")

def ask_broker(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'selected_assets': []}
    
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    markup.add('1. QUOTEX', '2. BINOLLA', '3. POCKET')
    msg = bot.send_message(chat_id, "📊 **BROKER SELECTION**\nSelect your broker:", reply_markup=markup, parse_mode='Markdown')
    bot.register_next_step_handler(msg, ask_market)

def ask_market(message):
    chat_id = message.chat.id
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    markup.add('1. QUOTEX OTC', '2. BINOLLA OTC', '3. REAL MARKET', '4. POCKET OTC')
    msg = bot.send_message(chat_id, "📊 **MARKET TYPE SELECTION**\nSelect market:", reply_markup=markup, parse_mode='Markdown')
    bot.register_next_step_handler(msg, ask_mtg)

def ask_mtg(message):
    chat_id = message.chat.id
    market = message.text
    if '1' in market: user_data[chat_id]['assets_list'] = QUOTEX_OTC_PAIR
    elif '2' in market: user_data[chat_id]['assets_list'] = BINOLLA_OTC_PAIR
    elif '3' in market: user_data[chat_id]['assets_list'] = REAL_MARKET_PAIR
    else: user_data[chat_id]['assets_list'] = POCKET_OTC_PAIR

    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    markup.add('1', '2', '3', '4', '5')
    msg = bot.send_message(chat_id, "📊 **MARTINGALE SETTINGS**\nSelect number of martingales per signal:", reply_markup=markup, parse_mode='Markdown')
    bot.register_next_step_handler(msg, ask_day_analysis)

def ask_day_analysis(message):
    chat_id = message.chat.id
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    markup.add('2', '3', '4', '6', '8', '12', '14')
    msg = bot.send_message(chat_id, "📊 **DAY ANALYSIS SETTINGS**\nSelect analysis period (Days):", reply_markup=markup, parse_mode='Markdown')
    bot.register_next_step_handler(msg, ask_news_filter)

def ask_news_filter(message):
    chat_id = message.chat.id
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    markup.add('1. Enable News & Trend Filter', '2. Disable News & Trend Filter')
    msg = bot.send_message(chat_id, "📊 **NEWS & TREND FILTER**\nSelect choice:", reply_markup=markup, parse_mode='Markdown')
    bot.register_next_step_handler(msg, ask_direction)

def ask_direction(message):
    chat_id = message.chat.id
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    markup.add('1. CALL Only', '2. PUT Only', '3. Both CALL and PUT')
    msg = bot.send_message(chat_id, "📊 **TRADING DIRECTION**\nSelect choice:", reply_markup=markup, parse_mode='Markdown')
    bot.register_next_step_handler(msg, ask_assets)

def ask_assets(message):
    chat_id = message.chat.id
    direction = message.text
    if '1' in direction: user_data[chat_id]['direction'] = '1'
    elif '2' in direction: user_data[chat_id]['direction'] = '2'
    else: user_data[chat_id]['direction'] = '3'

    assets = user_data[chat_id]['assets_list']
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    for asset in assets:
        markup.add(KeyboardButton(asset))
    markup.add(KeyboardButton('✅ Done (I finished adding)'))
    
    msg = bot.send_message(chat_id, "📊 **ASSET SELECTION**\nClick on the pairs you want to add. When finished, click '✅ Done':", reply_markup=markup, parse_mode='Markdown')
    bot.register_next_step_handler(msg, collect_assets)

def collect_assets(message):
    chat_id = message.chat.id
    text = message.text

    if text == '✅ Done (I finished adding)':
        if not user_data[chat_id]['selected_assets']:
            user_data[chat_id]['selected_assets'] = user_data[chat_id]['assets_list']
        ask_strategy(message)
    elif text in user_data[chat_id]['assets_list']:
        if text not in user_data[chat_id]['selected_assets']:
            user_data[chat_id]['selected_assets'].append(text)
            bot.send_message(chat_id, f"✅ Added: {text}")
        bot.register_next_step_handler(message, collect_assets)
    else:
        bot.register_next_step_handler(message, collect_assets)

def ask_strategy(message):
    chat_id = message.chat.id
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    markup.add('1. 1ST Strategy', '2. 2ND Strategy', '3. 3RD Strategy', '4. 5M SIGNALS ONLY', '5. 6TH HARD STRATEGY', '6. Random Strategy')
    msg = bot.send_message(chat_id, "📊 **SIGNAL STRATEGY SELECTION**\nSelect strategy:", reply_markup=markup, parse_mode='Markdown')
    bot.register_next_step_handler(msg, ask_total_signals)

def ask_total_signals(message):
    chat_id = message.chat.id
    strategy = message.text
    
    if '1' in strategy: user_data[chat_id]['strategy'] = '1'
    elif '2' in strategy: user_data[chat_id]['strategy'] = '2'
    elif '3' in strategy: user_data[chat_id]['strategy'] = '3'
    elif '4' in strategy: user_data[chat_id]['strategy'] = '4'
    elif '5' in strategy: user_data[chat_id]['strategy'] = '5'
    else: user_data[chat_id]['strategy'] = '6'

    markup = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True)
    markup.add('10', '25', '50', '100')
    msg = bot.send_message(chat_id, "📊 **SIGNAL GENERATION**\nHow many signals to generate? (Type a number 1-100):", reply_markup=markup, parse_mode='Markdown')
    bot.register_next_step_handler(msg, generate_and_send)

def generate_and_send(message):
    chat_id = message.chat.id
    try:
        total_signals = int(message.text)
    except:
        total_signals = 10
        
    bot.send_message(chat_id, "⏳ Status: Kiser GENERATING SIGNALS...", reply_markup=ReplyKeyboardRemove())
    
    data = user_data[chat_id]
    df = generate_signals(data['selected_assets'], total_signals, data['direction'], data['strategy'])
    
    response = "```text\n"
    response += "Signals List:\n"
    response += df.to_string(index=False)
    response += "\n```"
    
    calls = len(df[df['Direction'] == 'CALL'])
    puts = len(df[df['Direction'] == 'PUT'])
    call_pct = (calls / len(df)) * 100
    put_pct = (puts / len(df)) * 100
    
    summary = "```text\n"
    summary += "═══════════════════════════\n"
    summary += "      SIGNALS SUMMARY      \n"
    summary += "═══════════════════════════\n"
    summary += f"Total Signals: {len(df)}\n"
    summary += f"CALL Signals: {calls}\n"
    summary += f"PUT Signals: {puts}\n"
    summary += f"Distribution: CALL {call_pct:.1f}% | PUT {put_pct:.1f}%\n"
    summary += "═══════════════════════════\n"
    summary += "© 2030 Kiser OTC | All Rights Reserved\n```"

    bot.send_message(chat_id, response, parse_mode='Markdown')
    bot.send_message(chat_id, summary, parse_mode='Markdown')
    bot.send_message(chat_id, "🔄 To start a new session, send /start")

# ==========================================
# 5. تشغيل البوت
# ==========================================
if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
