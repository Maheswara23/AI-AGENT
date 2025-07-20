# AI-AGENT

# 🤖 Jarvis – Voice Assistant for Mobile Automation

**Jarvis** is an always-on voice assistant built in Python that listens for the wake word **"jarvis"** and lets you automate your Android device over ADB.  
You can open apps, play YouTube videos, or send WhatsApp messages — all through natural voice commands.

---

## ✨ Features

✅ **Wake word detection**: "jarvis" triggers the assistant to start listening for your commands.  
✅ **Connects to Android device** automatically over Wi-Fi using ADB.  
✅ **Understands commands** like:
- "Open VS Code"
- "Play [song] on YouTube"
- "Send message to [contact]"
- "Phone call to [contact]"
- "Video call to [contact]"

✅ **Database driven**: Store your apps, contacts, and favorite websites in SQLite.  
✅ **Device automation**: Uses ADB to tap, type, or send key events.

---

## 🧩 Project Structure

```text
📦 jarvis-voice-assistant
├── listener.py            # Listens for wake word using Vosk
├── main.py                # Connects device & starts command loop
├── engine/
│   ├── auto_adb.py        # Connects to Android device over ADB
│   ├── command.py         # Voice command recognition & routing
│   ├── helper.py          # ADB automation helpers
│   ├── db.py              # Initialize database & sample inserts
│   ├── db_utils.py        # Database connection utility
│   ├── voice.py           # Text-to-speech helper
│   └── features.py        # Handlers: open apps, YouTube, WhatsApp
├── database.db            # SQLite database (auto created)
├── run_listener.bat       # Windows batch to start listener
└── device.bat             # Batch file to manage device connection
```

---

## ⚙️ How It Works
**Start listener:**

```bash
   python listener.py
```
or run run_listener.bat.

**Wake word detection:**

Listens for the word "jarvis" using the Vosk speech recognition engine.

**Device connection:**

main.py connects to your Android device over ADB Wi-Fi.

**Voice command:**

Use natural commands like:

- "Open Chrome"
- "Play cricket on Youtube"
- "Send message to [contact]"

**Execution:**

The assistant opens apps, plays videos, or sends messages based on what you said.

---

## 🛠 Installation & Setup

**📥 Clone the project**

```bash
git clone https://github.com/yourusername/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

**🧰 Install dependencies**

```bash
pip install vosk sounddevice SpeechRecognition
```

**📦 Download Vosk Model**

Download a model (e.g., vosk-model-small-en-us-0.15) and place it inside:

```bash
model/vosk-model-small-en-us-0.15
```

**📱 Prepare Android device**

- Enable Developer Options

- Enable USB debugging and Wireless debugging

- Ensure your PC can reach your device over network

**🛠 Connect device**

Edit engine/auto_adb.py to set your device IP if needed:

```bash
device_ip='10.84.185.17'
```

**🗂 Database**

The assistant uses an SQLite database (database.db) to store:

- 🖥 Local apps (sys_command)

- 🌐 Web URLs (web_command)

- 📇 Contacts (contacts)

Edit engine/db.py to add your apps, sites, or contacts, or use any SQLite editor.

**🧪 Example Commands**

| Voice Command               | Action                                        |
| --------------------------- | --------------------------------------------- |
| “Open VS Code”              | Launches VS Code (configured in sys\_command) |
| “Play despacito on YouTube” | Searches and plays on YouTube                 |
| “Send message to [contact]”    | Prompts for message text, sends via WhatsApp  |
| “Phone call to [contact]”      | Starts call via WhatsApp                      |
| “Video call to [contact]”      | Starts video call via WhatsApp                |

**✅ Requirements**

- Python 3.7+

- Vosk speech recognition model

- ADB installed & added to PATH

- Android device with debugging enabled

