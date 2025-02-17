# Amaze Bot

Amaze Bot is a Telegram chatbot powered by NVIDIA's LLaMA model, designed for intelligent and interactive conversations. Built using Aiogram and OpenAI APIs, it supports commands for starting conversations, clearing context, and providing assistance.

---

## Features
- **AI-powered chat** using NVIDIA's LLaMA model.
- **Command-based interactions** (`/start`, `/clear`, `/help`).
- **Maintains conversation history** for contextual replies.
- **Easy setup and deployment** with environment variables.

---

## Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/pdobariya1/TelegramBot.git
cd telegrambot
```

### 2. Create a Virtual Environment
```bash
conda create -p {env_name} python=3.10.16 -y
conda activate ./{env_name}
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt --use-pep517
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add:
```bash
TELEGRAM_BOT_API=your_telegram_bot_token
NVIDIA_API=your_nvidia_api_key
```

### 5. Run the Bot
```bash
python main.py
```

---

## Commands
- **/start** – Start the bot.
- **/clear** – Clear previous conversation history.
- **/help** – Display available commands.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

