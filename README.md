## 🤖 DetectBotWithBrowserString

A lightweight Python tool to **detect bots and crawlers** using **User-Agent string matching** with **regex patterns** and **static lists**.

> Designed for simplicity, speed, and customization. Ideal for filtering crawlers from web traffic or logs.

---

### 📌 Key Features

* 🔍 Detect bots using known regex signatures (`crawler-user-agents.json`)
* 📜 Compare against a curated list of known bot strings (`user-agents-bots.txt`)
* 🛠️ Easily extend with your own patterns via `custom.json`
* ✅ Uses only Python's built-in libraries — **no external dependencies**

---

### 🧠 How It Works

The tool performs **two checks** on any User-Agent string:

1. **Exact Match**:

   * Checks if the string is found in the `user-agents-bots.txt` file.
2. **Regex Match**:

   * Uses regex patterns from `crawler-user-agents.json` to match bot-like strings.
   * (Support for `custom.json` is built-in but currently commented out.)

---

### 🗂️ Project Structure

```bash
DetectBotWithBrowserString/
│
├── isbot.py                   # Main detection script
├── crawler-user-agents.json   # Regex patterns for common bots
├── user-agents-bots.txt       # List of known bot user-agent strings
├── custom.json                # (Optional) Your custom bot patterns
└── README.md                  # Documentation
```

---

### 🛠️ Usage

#### 1. **Basic Python Usage**

```python
from isbot import check

ua = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

if check(ua):
    print("Detected as bot/crawler!")
else:
    print("Legitimate user.")
```

#### 2. **Running as a script**

```bash
python isbot.py
```

Sample output:

```
User-agent is not recognized as a bot.
```

---

### 📁 File Formats Explained

#### 🔹 `crawler-user-agents.json`

```json
[
  { "pattern": "bot" },
  { "pattern": "crawler" },
  { "pattern": "spider" }
]
```

Regex-based matching against User-Agent strings.

---

#### 🔹 `user-agents-bots.txt`

```
Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
curl/7.64.1
python-requests/2.23.0
```

Exact match — line-by-line check.

---

#### 🔹 `custom.json` (Optional)

> Not enabled by default — uncomment the relevant lines in `isbot.py` to use.

```json
[
  { "pattern": "mycustombot" },
  { "pattern": "weird-crawler-xyz" }
]
```

---

### ⚙️ Customize the Detector

To use your own bot patterns:

1. Add your regex patterns to `custom.json`.
2. Uncomment the relevant block in `isbot.py`:

   ```python
   custom_user_agents = json.loads(load_file('custom.json'))
   ...
   for definition in custom_user_agents:
       ...
   ```

---

### 🧪 Example Test Cases

```python
ua_bot = "curl/7.64.1"
ua_user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."

check(ua_bot)   # True
check(ua_user)  # False
```

---

### ✅ Requirements

* Python 3.x
* Uses only standard libraries: `re`, `json`

---

### 🚧 Future Enhancements

* [ ] Enable dynamic loading of `custom.json` by default
* [ ] Add CLI interface for bulk checking
* [ ] Add logging and confidence scores

