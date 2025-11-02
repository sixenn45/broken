import random
import time

class MessageGenerator:
    def __init__(self):
        self.message_pools = {
            'indonesia': [
                "ada yang baru @jilbabketat? 😊",
                "kuyy join bro @jilbabketat 💬",
                "@jilbabketat info terbaru ga? 🔥",
                "Semangat hari ini guys! t.me/jilbabketat💪",
                "gabungg yuk @jilbabketat! 🎯",
                "hay ka @jilbabketat 🤔",
                "Lagi pada ngapain nih? 🎮",
                "Ada rekomendasi film bagus? 🎬",
                "Musik favorit kalian apa? @jilbabketat 🎵",
                "Makanan enak apa hari ini? @jilbabketat 🍔"
            ],
            'random': [
                "Hello everyone! @jilbabketat How's it going? 🌟",
                "Interesting discussion! @jilbabketat 💭",
                "Any updates? @jilbabketat 📢",
                "Keep up the good work! @jilbabketatat"
            ]
        }
        
        self.sent_messages = []
    
    def get_random_message(self):
        """Generate random message yang belum pernah dikirim recently"""
        # Gabung semua message pools
        all_messages = self.message_pools['indonesia'] + self.message_pools['random']
        
        # Filter messages yang belum dikirim dalam 1 jam terakhir
        current_time = time.time()
        recent_messages = [msg for msg in self.sent_messages 
                          if msg['time'] > current_time - 3600]
        recent_texts = [rm['text'] for rm in recent_messages]
        
        # Pilih message yang belum recent
        available_messages = [msg for msg in all_messages if msg not in recent_texts]
        
        # Jika semua message sudah dipakai, reset
        if not available_messages:
            available_messages = all_messages
            self.sent_messages = []
        
        chosen_message = random.choice(available_messages)
        
        # Simpan ke history
        self.sent_messages.append({
            'text': chosen_message,
            'time': current_time
        })
        
        # Keep history manageable (max 50 messages)
        self.sent_messages = self.sent_messages[-50:]
        
        return chosen_message
