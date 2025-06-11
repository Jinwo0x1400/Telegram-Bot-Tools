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

✅ Load your .session
✅ Read scraped users from teammember.csv
✅ Add them to a target group
✅ Wait between adds
✅ Log success/fail results

### ✅ How to Use
```
python adder.py
```

### 🧠 Suggestion: Try with 2–3 users first, then increase gradually. Always rotate accounts and sleep between adds to avoid getting banned.
