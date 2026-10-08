# Bunker Bot

Telegram-бот для гри в "Бункер": генерує персонажів, сценарії та параметри бункера.

## Локальний запуск

1. Створи віртуальне середовище:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Встанови залежності:

```bash
pip install -r requirements.txt
```

3. Створи `.env` на основі `.env.example`:

```bash
cp .env.example .env
```

4. Встав свій Telegram bot token у `.env`:

```env
BOT_TOKEN=your_telegram_bot_token
PERSON_COOLDOWN_SECONDS=300
```

5. Запусти бота:

```bash
python main.py
```

## Деплой

Інструкція для Ubuntu/VPS є в [DEPLOY.md](DEPLOY.md).

## Важливо

Не коміть `.env` і не вставляй `BOT_TOKEN` напряму в код. Файл `.env` має залишатися тільки локально або на сервері.
