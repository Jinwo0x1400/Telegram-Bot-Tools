# Telegram-Bot-Tools
🤖 Jinwoo Telegram Bot Tools: Scraper, Adder, Message Sender

### ✅ Project Structure 
- telegram-tools/
- ├── auth.py           # Login with phone number (OTP)
- ├── scrape.py         # Scrape group members
- ├── adder.py          # Add users to group
- ├── sender.py         # Send message to users
- ├── numbers.csv       # List of accounts (API_ID, API_HASH, phone)
- ├── teammember.csv    # Scraped users
- ├── message.txt       # Message content to send
- ├── credentials.txt   # Optional log of verified accounts
- ├── README.md

### 📦 Dependencies
```python
pip install telethon
```
## 📦 Daftar Isi

- 📌[Laravel Artisan Cheatsheet](./laravel.md)
- 📌[PHP Snippets](./php.md)
- 📌[Shell Command](./shell.md)
- 📌[SQL Query Collection](./sql.md)
- 📌[Python Handy Scripts](./python.md)
- 📌[JavaScript Tricks](./javascript.md)

### [authentication](./auth.py)

📝 Output:
- .session file saved with name based on phone (e.g. 62812345.session)

- Verified accounts recorded in credentials.txt like:
```
+62812345,123456,abc123def456,62812345.session
```
