# Jinwwoo Telegram Bot Authentication(auth)
# https://github.com/Jinwo0x1400/Telegram-Bot-Tools

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

def main():
    print("=== Telegram Auth Tool ===")

    api_id = int(input("Enter API ID: ").strip())
    api_hash = input("Enter API HASH: ").strip()
    phone = input("Enter your phone number (with country code): ").strip()

    session_name = phone.replace('+', '')
    client = TelegramClient(session_name, api_id, api_hash)

    try:
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            code = input("Enter the OTP code: ").strip()
            client.sign_in(phone, code)

        print(f"[✔] Login successful for {phone}")
        client.disconnect()

        # Save to credentials.txt
        with open("credentials.txt", "a") as f:
            f.write(f"{phone},{api_id},{api_hash},{session_name}.session\n")

    except Exception as e:
        print(f"[✖] Login failed: {e}")

if __name__ == "__main__":
    main()
