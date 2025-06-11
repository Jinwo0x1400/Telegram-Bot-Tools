# Jinwoo Telegram Bot Add member to group (adder)
# https://github.com/Jinwo0x1400/Telegram-Bot-Tools

import os
import sys
from colorama import init, Fore, Style

init(autoreset=True)

def show_banner():
    print(Fore.MAGENTA + Style.BRIGHT + r"""
      ██╗██╗███╗   ██╗██╗    ██╗ ██████╗  ██████ 
      ██║██║████╗  ██║██║    ██║██╔═══██╗██╔═══██║
      ██║██║██╔██╗ ██║██║ █╗ ██║██║   ██║██║   ██║
 ██   ██║██║██║╚██╗██║██║███╗██║██║   ██║██║   ██║
 ╚█████╔╝██║██║ ╚████║╚███╔███╔╝╚██████╔╝╚██████╔╝
  ╚════╝ ╚═╝╚═══╝╚═╝╚═╝  ╚═══╝ ╚══╝╚══╝  ╚═════╝  ╚═════╝ 
🤖 JINWOO TELEGRAM BOT TOOLKIT - Scraper | Adder | Sender
    https://github.com/Jinwo0x1400/Telegram-Bot-Tools/
    """ + Style.RESET_ALL)

def menu():
    print(Fore.CYAN + """
===============================
  🧭 Main Menu
===============================
[1] 🔐 Login & Save Session
[2] 👥 Scrape Group Members
[3] ➕ Add Users to Group
[4] 💌 Send Private Messages
[0] ❌ Exit
""")

def run(command):
    try:
        os.system(f"python {command}")
    except Exception as e:
        print(Fore.RED + f"Error running {command}: {e}")

def main():
    show_banner()
    while True:
        menu()
        choice = input(Fore.YELLOW + "Choose option: ").strip()
        if choice == '1':
            run("auth.py")
        elif choice == '2':
            run("scrape.py")
        elif choice == '3':
            run("adder.py")
        elif choice == '4':
            run("sender.py")
        elif choice == '0':
            print(Fore.GREEN + "Goodbye!")
            sys.exit(0)
        else:
            print(Fore.RED + "Invalid choice!")

if __name__ == "__main__":
    main()
