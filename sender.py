# Jinwwoo Telegram Bot Authentication(auth)
# https://github.com/Jinwo0x1400/Telegram-Bot-Tools

import csv
import time
import random
from telethon.sync import TelegramClient
from telethon.errors import (
    PeerFloodError,
    UserPrivacyRestrictedError,
    FloodWaitError
)
from telethon.tl.functions.messages import SendMessageRequest

def main():
    print("=== Telegram Message Sender ===")

    session_file = input("Enter phone/session file (e.g. 62812345): ").strip()
    api_id = int(input("Enter API ID: ").strip())
    api_hash = input("Enter API HASH: ").strip()
    min_delay = int(input("Wait time MIN (sec): ") or 30)
    max_delay = int(input("Wait time MAX (sec): ") or 60)

    with open("message.txt", "r", encoding='utf-8') as f:
        message = f.read().strip()

    if not message:
        print("[✖] message.txt is empty.")
        return

    client = TelegramClient(session_file, api_id, api_hash)
    client.start()

    with open("teammember.csv", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        users = [row for row in reader if row['username']]  # skip users with no username

    print(f"[✔] Loaded {len(users)} users with usernames.")

    for idx, user in enumerate(users):
        username = user['username']
        try:
            print(f"[{idx+1}] Sending message to @{username}...", end=" ")
            entity = client.get_entity(username)
            client(SendMessageRequest(entity=entity, message=message, no_webpage=True))
            print("✅ Sent")

        except UserPrivacyRestrictedError:
            print("🔒 User has privacy settings")
        except PeerFloodError:
            print("💥 Flood error — stopping to avoid ban")
            break
        except FloodWaitError as e:
            print(f"⏳ FloodWait: sleeping {e.seconds} seconds")
            time.sleep(e.seconds)
        except Exception as e:
            print(f"❌ Error: {e}")

        delay = random.randint(min_delay, max_delay)
        print(f"⏱ Waiting {delay}s before next...")
        time.sleep(delay)

    client.disconnect()
    print("All done.")

if __name__ == "__main__":
    main()
