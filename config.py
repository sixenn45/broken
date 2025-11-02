import os

# Configuration settings
class Config:
    # Telegram API credentials (akan diambil dari environment variables)
    API_ID = int(os.getenv('API_ID', '1234567'))
    API_HASH = os.getenv('API_HASH', 'your_api_hash_here')
    PHONE_NUMBER = os.getenv('PHONE_NUMBER', '+6281234567890')
    
    # Bot settings
    MIN_DELAY = 30  # Minimum delay antara pesan (detik)
    MAX_DELAY = 90  # Maximum delay antara pesan (detik)
    LONG_BREAK_MIN = 600  # Minimum break antara loop (detik)
    LONG_BREAK_MAX = 900  # Maximum break antara loop (detik)
    
    # Target groups (GANTI DENGAN GRUP KAMU)
    TARGET_GROUPS = [
        '@testgroup123',
        '@spamgroup456', 
        '@randomgroup789'
    ]
