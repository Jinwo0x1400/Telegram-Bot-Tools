# Jinwwoo Telegram Bot scraping(scrape)
# https://github.com/Jinwo0x1400/Telegram-Bot-Tools

from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import csv
import os

def main():
    print("=== Telegram Group Scraper ===")

    session_file = input("Enter phone or session filename (e.g. 62812345): ").strip()
    api_id = int(input("Enter API ID: ").strip())
    api_hash = input("Enter API HASH: ").strip()

    client = TelegramClient(session_file, api_id, api_hash)
    client.start()

    group_input = input("Enter group username or ID (e.g. @examplegroup): ").strip()
    limit = int(input("How many members to scrape? (e.g. 5000): ") or 5000)

    try:
        entity = client.get_entity(group_input)
        participants = client(GetParticipantsRequest(
            channel=entity,
            filter=ChannelParticipantsSearch(''),
            offset=0,
            limit=limit,
            hash=0
        )).users

        print(f"[✔] Found {len(participants)} members. Saving to teammember.csv...")

        with open("teammember.csv", "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["user_id", "username", "access_hash", "name"])
            for user in participants:
                writer.writerow([
                    user.id,
                    user.username or "",
                    user.access_hash,
                    f"{user.first_name or ''} {user.last_name or ''}".strip()
                ])

        print("[✔] Done. File saved as teammember.csv")

    except Exception as e:
        print(f"[✖] Error: {e}")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()

