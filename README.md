# Telegram-Bot-Tools
🤖 Jinwoo Telegram Bot Tools: Scraper, Adder, Message Sender

### ✅ Project Structure 
- telegram-tools/
- ├── auth.py           # Login with phone number (OTP)
- ├── scrape.py         # Scrape group members
- ├── adder.py          # Add users to group
- ├── sender.py         # Send message to users
- ├── setup.py          # Setup module and this is the first thing to do ✅
- ├── numbers.csv       # List of accounts (API_ID, API_HASH, phone)
- ├── teammember.csv    # Scraped users
- ├── message.txt       # Message content to send
- ├── credentials.txt   # Optional log of verified accounts
- ├── README.md



### 📦 Dependencies
```python
pip install -r requirements.txt
```

### Optional: Enhance your scripts using colorama for better terminal output:
## Add all this code into your code (
```
from colorama import init, Fore
init(autoreset=True)
print(Fore.GREEN + "✅ Success")
print(Fore.RED + "❌ Failed")
```

### Python 3.8+ recommended.
[Download Python](https://www.python.org/downloads/)

### 🚀 How to Use
- 1. Login & Save Session
```
python auth.py
```
- 2. Scrape Members from Group
```
python scrape.py
```
- 3. Add Users to Your Group
```
python adder.py
```
- 4. Send Messages to Users
```
python sender.py
```

### [Authentication](./auth.py)

📝 Output:
- .session file saved with name based on phone (e.g. 62812345.session)

- Verified accounts recorded in credentials.txt like:
```
+62812345,123456,abc123def456,62812345.session
```

### [SCRAPING](./scrape.py)
- 📝 Output: teammember.csv
```
user_id	        username	      access_hash	              name
123456789	      johndoe	    1313218491832891	         John Doe
```
### ✅ How to Run
```
python scrape.py
```

### [Add Member to group](./adder.py)
### adder.py script — it will:

- ✅ Load your .session
- ✅ Read scraped users from teammember.csv
- ✅ Add them to a target group
- ✅ Wait between adds
- ✅ Log success/fail results

### ✅ How to Use
```
python adder.py
```

### 🧠 Suggestion: Try with 2–3 users first, then increase gradually. Always rotate accounts and sleep between adds to avoid getting banned.

### [Sender Message](./sender.py)

### This script will:

- ✅ Use your .session
- ✅ Load teammember.csv
- ✅ Read message.txt
- ✅ Send private message to each user
- ✅ Skip users without username (to avoid delivery failure)
- ✅ Sleep between sends
- ✅ Log status to console

### 📝 Required:
- teammember.csv: must include usernames

- message.txt: the full message you want to send

- Example message.txt:
```
Hello 👋
Join our private group for exclusive content: https://t.me/yourgroup
```

### 🚀 How to Run
```
python sender.py
```

### ⚠️ Disclaimer
- Use responsibly. Abuse may lead to Telegram account bans.
- Do not use this tool to spam or violate Telegram Terms of Service.


### 🧠 Author
Made with 💻 by Jinwoo | [GitHub - Telegram Adder - Scrape - Sender Message - Rotate Account ](https://github.com/Jinwo0x1400/Telegram-Bot-Tools)
