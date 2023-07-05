# telebard

This repository contains code that implements a Telegram chatbot using the `bardapi` library and the `python-telegram-bot` library. The chatbot utilizes the BARD API to provide responses to user messages.

## Installation

To run the code in this repository, you need to install the following dependencies:

- `bardapi`: Use the following command to install the `bardapi` library:
  ```
  pip install bardapi
  ```

- `python-telegram-bot`: Use the following command to install the `python-telegram-bot` library version 12.8:
  ```
  pip install python-telegram-bot==12.8
  ```

## Usage

1. Obtain a Telegram Bot Token: 
   - Create a new bot on Telegram by contacting the BotFather ([https://t.me/BotFather](https://t.me/BotFather)).
   - Follow the instructions to create a new bot and obtain a token.

2. Set the Bot Token:
   - In the code, replace `'YOUR_TELEGRAM_BOT_TOKEN'` with the token you obtained from the BotFather. The token should be assigned to the `token` variable.

3. Set the BARD Token:
   - Visit https://bard.google.com/
   - F12 for console
   - Session: Application → Cookies → Copy the value of __Secure-1PSID cookie.
   - Replace `'YOUR_BARD_TOKEN'` with the value of __Secure-1PSID cookie. The token should be assigned to the `token_bard` variable.

4. Run the Code:
   - Execute the Python script to run the Telegram bot:
     ```
     python script_name.py
     ```

## Functionality

The Telegram chatbot provides the following functionality:

- `/start` command: Sends a greeting message to the user.

- Answering User Messages: The bot processes user messages and sends a response using the BARD API.
  - It simulates typing by showing a typing animation.
  - It waits for 2 seconds to simulate processing time.
  - The response can include text, code snippets, and images.
    - Text Response: The bot sends the text response back to the user.
    - Code Response: If the response includes code, the bot sends the code back to the user enclosed in triple backticks (```). 
    - Image Response: If the response includes links to images, the bot sends up to 5 images back to the user.

## Contributions

Contributions to this repository are welcome. If you find any issues or have suggestions for improvement, feel free to create a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).
