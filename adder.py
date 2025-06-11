# Jinwwoo Telegram Bot Authentication(auth)
# https://github.com/Jinwo0x1400/Telegram-Bot-Tools

import csv
import time
import random
from telethon.sync import TelegramClient
from telethon.errors import (
    PeerFloodError,
    UserPrivacyRestrictedError,
    UserAlreadyParticipantError,
    UserBannedInChannelError,
    FloodWaitError
)
from telethon.tl.functions.channels import InviteToChannelRequest

def main():
    print("=== Telegram Group Adder ===")

    session_file = input("Enter phone/session file (e.g. 62812345): ").strip()
    api_id = int(input("Enter API ID: ").strip())
    api_hash = input("Enter API HASH: ").strip()
    group_username = input("Enter target group username (e.g. @mygroup): ").strip()

    wait_min = int(input("Wait time MIN (sec): ") or 60)
    wait_max = int(input("Wait time MAX (sec): ") or 90)

    client = TelegramClient(session_file, api_id, api_hash)
    client.start()

    try:
        entity = client.get_entity(group_username)
    except Exception as e:
        print(f"[✖] Failed to get group: {e}")
        return

    users = []
    with open("teammember.csv", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append(row)

    print(f"[✔] Loaded {len(users)} users from teammember.csv")

    for index, user in enumerate(users):
        try:
            print(f"[{index+1}] Adding {user['username']}...", end=' ')
            user_id = int(user['user_id'])
            access_hash = int(user['access_hash'])

            client(InviteToChannelRequest(entity, [client.get_input_entity((user_id, access_hash))]))
            print("✅ Success")

        except UserAlreadyParticipantError:
            print("⏭️ Already in group")
        except UserPrivacyRestrictedError:
            print("🔒 Privacy restricted")
        except UserBannedInChannelError:
            print("🚫 Banned in channel")
        except PeerFloodError:
            print("💥 PeerFloodError - Stopping")
            break
        except FloodWaitError as e:
            print(f"⏳ Telegram rate limit: wait {e.seconds}s")
            time.sleep(e.seconds)
        except Exception as e:
            print(f"❌ Error: {e}")

        delay = random.randint(wait_min, wait_max)
        print(f"⏱ Waiting {delay}s...")
        time.sleep(delay)

    client.disconnect()
    print("Done.")

if __name__ == "__main__":
    main()
