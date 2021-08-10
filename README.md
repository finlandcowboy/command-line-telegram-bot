<h1 align="center">Welcome to Command Line Telegram Bot 👋</h1>
<p>
</p>

> This bot would help you to execute commands on your server from Telegram Client

## Install

```sh
git clone https://github.com/finlandcowboy/command-line-telegram-bot 
chmod +x build.sh
./build.sh
```

## Usage

In ```config.txt```
First line argument is <b>YOUR_BOT_TOKEN</b>
Second line argument is <b>YOUR_CHAT_ID</b>
```
./build.sh
```

```
sudo apt-get install screen
screen -dmS ServerBot python3 bot.py -token config.txt
```

If you want to stop bot
```
screen -S ServerBot -X quit
```

## Author

👤 **Zhashkov Stepan**

* Github: [@finlandcowboy](https://github.com/finlandcowboy)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_