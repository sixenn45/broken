from telethon import TelegramClient
import asyncio
import random
import os
import sys
from message_generator import MessageGenerator
from config import Config

print("🚀 Starting Telegram UserBot via GitHub Actions...")

try:
    api_id = int(os.environ['API_ID'])
    api_hash = os.environ['API_HASH']
    phone_number = os.environ['PHONE_NUMBER']
    
    print(f"✅ Credentials loaded for: {phone_number}")
    
    # Session file di folder session
    client = TelegramClient('session/user_session', api_id, api_hash)
    msg_gen = MessageGenerator()
    
except Exception as e:
    print(f"❌ Error loading credentials: {e}")
    sys.exit(1)

async def main():
    try:
        await client.start(phone_number)
        print("✅ UserBot started!")
        
        # Kirim pesan ke grup
        for group in Config.TARGET_GROUPS:
            try:
                message = msg_gen.get_random_message()
                await client.send_message(group, message)
                print(f"📨 Sent to {group}: {message}")
                
                # Delay random
                delay = random.randint(Config.MIN_DELAY, Config.MAX_DELAY)
                print(f"⏰ Waiting {delay} seconds...")
                await asyncio.sleep(delay)
                
            except Exception as e:
                print(f"❌ Error sending to {group}: {e}")
                await asyncio.sleep(30)
                
        print("🎯 Mission completed!")
        
    except Exception as e:
        print(f"💀 Fatal error: {e}")
    finally:
        await client.disconnect()
        print("🔚 Bot disconnected")

if __name__ == "__main__":
    asyncio.run(main())
