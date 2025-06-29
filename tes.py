import os
import time

def record_screen(duration=10):
    print("[*] Merekam layar selama", duration, "detik...")
    os.system(f"screenrecord --time-limit {duration} /sdcard/wa_viewonce_capture.mp4")
    print("[+] Video disimpan ke /sdcard/wa_viewonce_capture.mp4")

def take_screenshot():
    timestamp = int(time.time())
    path = f"/sdcard/wa_viewonce_{timestamp}.png"
    os.system(f"screencap -p {path}")
    print(f"[+] Screenshot disimpan: {path}")

def menu():
    while True:
        print("""
==== WA ViewOnce Capture ====
1. Screenshot (langsung)
2. Rekam layar (10 detik)
3. Keluar
""")
        choice = input("Pilih opsi: ")
        if choice == '1':
            take_screenshot()
        elif choice == '2':
            record_screen()
        elif choice == '3':
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()