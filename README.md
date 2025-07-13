Telegram Bot for Sending PDF by Payment Code
This Telegram bot receives a payment code from the user and sends the corresponding PDF file if the code is valid.

How It Works
The user starts the bot with the /start command.

The bot welcomes the user and asks to send the payment code.

The user sends a code.

If the code exists in the code_to_file dictionary, the bot sends the associated PDF file.

If the code is invalid, the bot replies with an error message.

Installation and Running
Clone the repository or copy the project files.

Create a file named telegram_token.txt in the project root and paste your Telegram Bot API token there.

Place your PDF file(s) inside the telegram_bot/files/ folder (or update the path in the code_to_file dictionary).

Install dependencies:

pip install python-telegram-bot --upgrade
Run the bot:

python your_bot_file.py
Configuration
In the code_to_file dictionary, specify pairs of "payment_code": "path_to_pdf_file".

By default, the example includes the code "ABC123" linked to product.pdf.

Usage Example
Start the bot.

Send the /start command.

Send the code ABC123.

Receive the product.pdf file.

Requirements
Python 3.7+

python-telegram-bot library version 20+
