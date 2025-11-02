import os

class Config:
    # ⚡⚡⚡ FUCKING DELAY SETTINGS - EDIT DI SINI! ⚡⚡⚡
    
    # Delay antara pesan ke grup YANG SAMA (detik)
    MIN_DELAY = 30    # Minimal 30 detik
    MAX_DELAY = 90    # Maksimal 90 detik
    
    # Delay antara pesan ke grup BERBEDA (detik)  
    MIN_DELAY_DIFFERENT_GROUP = 10   # Minimal 10 detik
    MAX_DELAY_DIFFERENT_GROUP = 30   # Maksimal 30 detik
    
    # Long break setelah 1 cycle selesai (detik)
    LONG_BREAK_MIN = 600   # Minimal 10 menit
    LONG_BREAK_MAX = 900   # Maksimal 15 menit
    
    # Break setelah berapa banyak pesan
    BREAK_AFTER_MESSAGES = 5    # Break setelah 5 pesan
    BREAK_DURATION = 120        # Break duration 2 menit
    
    # ⚡⚡⚡ TARGET GRUP - GANTI DENGAN GRUP LU! ⚡⚡⚡
    TARGET_GROUPS = [
        '@cari_sahabat_teman_pacar',
        '@IndonesiaDefacer', 
        '@cari_pacar_teman_kenalan'
    ]
