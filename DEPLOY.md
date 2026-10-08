# Deploy

Інструкція для запуску Telegram-бота на одному Ubuntu/VPS сервері як постійного `systemd` сервісу.

## 1. Підготувати сервер

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
```

## 2. Завантажити проєкт

```bash
cd /opt
sudo git clone https://github.com/Axmetik/bunker.git
sudo chown -R $USER:$USER /opt/bunker
cd /opt/bunker
```

## 3. Встановити залежності

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Додати секрети

Створи `.env`:

```bash
nano .env
```

Приклад:

```env
BOT_TOKEN=your_telegram_bot_token
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_database_password
DB_NAME=bunker
```

Якщо база даних не використовується, значення `DB_*` можна лишити як у `.env.example`.

## 5. Перевірити запуск вручну

```bash
source .venv/bin/activate
python main.py
```

Зупинити: `Ctrl+C`.

## 6. Створити systemd service

```bash
sudo nano /etc/systemd/system/bunker-bot.service
```

Встав:

```ini
[Unit]
Description=Bunker Telegram Bot
After=network.target

[Service]
WorkingDirectory=/opt/bunker
EnvironmentFile=/opt/bunker/.env
ExecStart=/opt/bunker/.venv/bin/python /opt/bunker/main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

## 7. Запустити сервіс

```bash
sudo systemctl daemon-reload
sudo systemctl enable bunker-bot
sudo systemctl start bunker-bot
```

Перевірка:

```bash
sudo systemctl status bunker-bot
sudo journalctl -u bunker-bot -f
```

## 8. Оновлення після змін

```bash
cd /opt/bunker
git pull
source .venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart bunker-bot
```
