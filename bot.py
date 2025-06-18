import asyncio
import time
from telegram import Bot
from datetime import datetime
import requests

# === CONFIG ===
TELEGRAM_TOKEN = '7621886262:AAHpVs777HbQDXcVWsASFiujMvyxh7W7bY8'
CHAT_ID = '5745575076'
PAIR = 'XAU/USD'
GOLD_API_KEY = 'goldapi-5rdriosmc1fz3b7-io'

# === INIT TELEGRAM ===
bot = Bot(token=TELEGRAM_TOKEN)

# === FETCH PRICE FUNCTION ===
def get_price():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": GOLD_API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        print("🔍 Status Code:", response.status_code)
        print("🔍 Response Text:", response.text)
        data = response.json()
        price = data["price"]
        return round(price, 2)
    except Exception as e:
        print("❌ Error fetching price:", e)
        return None

# === SEND MESSAGE ASYNC FUNCTION ===
async def send_price_alert():
    price = get_price()
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"📈 {PAIR} Price Alert\nCurrent Price: ${price}\nTime: {time_now}"
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print("✅ Alert sent.")
    except Exception as e:
        print("❌ Failed to send alert:", e)

# === RUN THE ASYNC MAIN LOOP ===
async def main():
    print("🚀 Bot is running...")
    while True:
        await send_price_alert()
        await asyncio.sleep(60)  # Every 1 minute

# === START ===
if __name__ == "__main__":
    asyncio.run(main())
