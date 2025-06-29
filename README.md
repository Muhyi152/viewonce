# 📸 WA ViewOnce Capture (Termux Script)

Skript Python untuk mengambil **screenshot** atau **rekaman layar** otomatis pada pesan WhatsApp View Once (sekali lihat) via **Termux di Android**.

> ⚠️ Untuk keperluan edukasi dan riset pribadi. Jangan gunakan untuk pelanggaran privasi.

---

## ✨ Fitur
- Screenshot otomatis ke `/sdcard/` dengan nama berdasarkan timestamp
- Rekam layar otomatis selama 10 detik
- Menu CLI sederhana (langsung pakai di Termux)

---

## 📱 Cara Pakai di Termux

1. **Install Python dan Termux API**
   ```bash
   pkg update && pkg install python termux-api
