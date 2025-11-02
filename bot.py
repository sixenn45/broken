from telethon import TelegramClient
import asyncio
import random
import os
import time
from message_generator import MessageGenerator
from config import Config

print("🚀 Starting Telegram UserBot...")

# ⚡⚡⚡ AMBIL CREDENTIALS DARI ENVIRONMENT ⚡⚡⚡
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']) 
phone_number = os.environ['PHONE_NUMBER']

print(f"✅ Loaded credentials for: {phone_number}")

# Initialize client
client = TelegramClient('session', api_id, api_hash)
msg_gen = MessageGenerator()

async def fucking_send_messages():
    """Fucking function buat kirim message ke grup"""
    try:
        await client.start(phone_number)
        print("✅ UserBot started successfully!")
        
        message_count = 0
        
        for group in Config.TARGET_GROUPS:
            try:
                # Generate random message
                message = msg_gen.get_random_message()
                
                # Kirim message
                await client.send_message(group, message)
                message_count += 1
                print(f"📨 [{message_count}] Sent to {group}: {message}")
                
                # Delay setting
                if message_count % Config.BREAK_AFTER_MESSAGES == 0:
                    # Break setelah X pesan
                    print(f"💤 Break setelah {Config.BREAK_AFTER_MESSAGES} pesan: {Config.BREAK_DURATION} detik")
                    await asyncio.sleep(Config.BREAK_DURATION)
                else:
                    # Delay normal antara pesan
                    delay = random.randint(Config.MIN_DELAY, Config.MAX_DELAY)
                    print(f"⏰ Waiting {delay} seconds...")
                    await asyncio.sleep(delay)
                
            except Exception as e:
                print(f"❌ Error sending to {group}: {e}")
                await asyncio.sleep(60)
                
        return message_count
        
    except Exception as e:
        print(f"💀 Fatal error: {e}")
        return 0

async def main_loop():
    """Fucking main loop buat jalanin bot terus menerus"""
    print("🔄 Starting main loop...")
    
    total_messages = 0
    
    while True:
        try:
            messages_sent = await fucking_send_messages()
            total_messages += messages_sent
            
            print(f"📊 Cycle completed! Total messages: {total_messages}")
            
            # Long break antara cycle
            long_delay = random.randint(Config.LONG_BREAK_MIN, Config.LONG_BREAK_MAX)
            minutes = long_delay // 60
            print(f"💤 Long break: {long_delay} seconds ({minutes} minutes)")
            await asyncio.sleep(long_delay)
            
        except Exception as e:
            print(f"🔥 Loop error: {e}")
            await asyncio.sleep(300)

if __name__ == "__main__":
    print("🤖 Telegram UserBot Starting...")
    
    # Tampilkan setting saat start
    print("⚙️ Current Settings:")
    print(f"   Min Delay: {Config.MIN_DELAY}s")
    print(f"   Max Delay: {Config.MAX_DELAY}s") 
    print(f"   Long Break: {Config.LONG_BREAK_MIN}-{Config.LONG_BREAK_MAX}s")
    print(f"   Break after: {Config.BREAK_AFTER_MESSAGES} messages")
    print(f"   Target Groups: {len(Config.TARGET_GROUPS)} groups")
    
    asyncio.run(main_loop())
