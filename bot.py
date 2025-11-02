from telethon import TelegramClient
import asyncio
import random
import os
import time
from message_generator import MessageGenerator

print("🚀 Starting Telegram UserBot...")

# Config dari environment variables
api_id = int(os.getenv('API_ID', '1234567'))
api_hash = os.getenv('API_HASH', 'your_api_hash_here')
phone = os.getenv('PHONE_NUMBER', '+6281234567890')

# Initialize client
client = TelegramClient('session', api_id, api_hash)
msg_gen = MessageGenerator()

async def fucking_send_messages():
    """Fucking function buat kirim message ke grup"""
    try:
        await client.start(phone)
        print("✅ UserBot started successfully!")
        
        # Daftar grup target (GANTI DENGAN GRUP LU)
        groups = [
            '@testgroup123',
            '@spamgroup456',
            '@randomgroup789'
        ]
        
        for group in groups:
            try:
                # Generate random message
                message = msg_gen.get_random_message()
                
                # Kirim message
                await client.send_message(group, message)
                print(f"📨 Sent to {group}: {message}")
                
                # Random delay 30-90 detik (AMAN)
                delay = random.randint(30, 90)
                print(f"⏰ Waiting {delay} seconds...")
                await asyncio.sleep(delay)
                
            except Exception as e:
                print(f"❌ Error sending to {group}: {e}")
                await asyncio.sleep(60)  # Tunggu 1 menit jika error
                
    except Exception as e:
        print(f"💀 Fatal error: {e}")

async def main_loop():
    """Fucking main loop buat jalanin bot terus menerus"""
    print("🔄 Starting main loop...")
    
    while True:
        try:
            await fucking_send_messages()
            
            # Jeda 10-15 menit sebelum loop berikutnya
            long_delay = random.randint(600, 900)
            print(f"💤 Long break: {long_delay} seconds")
            await asyncio.sleep(long_delay)
            
        except Exception as e:
            print(f"🔥 Loop error: {e}")
            await asyncio.sleep(300)  # Tunggu 5 menit jika error

if __name__ == "__main__":
    print("🤖 Telegram UserBot Starting...")
    asyncio.run(main_loop())
