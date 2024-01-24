# B.A.D.A.S.S. Discord-Bot
### by Sylvan013 & Anderson4366

<img src="/docs/BADASS_Logo.png" alt="B.A.D.A.S.S. Logo" height="300" width="300"/>

Codename: B.A.D.A.S.S (**BA**dly coded **D**iscord **A**nnouncement **S**ystem for **S**ervers)

A little fun-project to make the world we live in a better place.

This bot can:
- Wish you good luck.
- Flame you.

This bot can't:
- Make your problems disappear (but it might help feeling better).
- Save you (from your demons. You can run, but you cannot hide).

## Functionalites
This bot is meant to flame people based on the champion they picked in League of Legends. This does not include all champions and some of the messages are also kind or just funny.

## Set up the bot[^1]
If you do not want to host the bot by your own, use [this link](https://discord.com/api/oauth2/authorize?client_id=1190361750755868692&permissions=687195285568&scope=bot).
To host the bot on your own, follow these steps:
1. Create a Discord application. If you don't know how to do this, look up the [Discord Developer Portal](https://discord.com/developers/docs/intro).
2. Replace the content of the file named `token.txt` in the `/resources` directory. This file shall contain only your bot-token. Noting else.
3. Create your database. Therefor download [MySQL Workbench](https://www.mysql.com/de/products/workbench/) and [MySQL Community Server](https://dev.mysql.com/downloads/mysql/). Configure them to your needs. For help look up the documentation on the respective websites.
4.  Replace the content of the file named `database_pw.txt` in the `/resources` directory. This file shall contain only your database password that you choose while setting up your mySQL database. Nothing else.
5. Run the `bot_main.py` file on the device you want to host the bot on.
### Modify the bot
The easiest way to modify the bot for your personal needs is to change the `config.json` file in the `/resources` directory.
You also can modify the code, if you know what you are doing. Just remain a clear reference to this original project in your modified code and link this repo in your new `README.md`.

## Commands
This bot uses several commands to be controlled:
- `!ping`: Bot respondes with *"Pong!"*. Can be used to check if the bot is working.
- `!status`: Bot respondes with *"HygeneBot is Online & registered on [Number of Servers the bot is active on] Servers"*.
- `!start`: Starts a loop, that looks over every server and sends messages if there is someone to blame. You can modify the iteration time for one loop in the `config.json` file in the `/resources` directory.
- `!initialize`: Bot respondes with *"Channel '[Channel Name]' created successfully Channel-ID: [Channel ID] Server-ID: [Server ID]"*. The bot also creates the channel that it will send its messages to. This command will only work once per server. If you host the bot by yourself, you can make the command work again by deleting the server file in the `/server` directory with the name that is equal to the server id from the server you want to use the command again.
- `!force_initialize`: Bot respondes *"Channel '[Channel Name]' created successfully Channel-ID: [Channel ID] Server-ID: [Server ID]"*. This command forces the bot to create a new channel to send messages in. You can use this e.g. if you deleted the initial channel.
>[!WARNING]
>`!force_initialize` is an experimental feature and may not lead to your desired outcome. If this command messes up something and you host the bot by yourself, clear the respective server files in the `/server` directory. If you invited the bot via the link above, please contact us via this [Reddit-Community](https://www.reddit.com/r/BADASS_Bot/).

>[!NOTE]
>If you look up the code, you will find some more commands that were used while developing this bot. Those commands are not needed for using the bot but we didn't want to delete them for people who might play arround with this.

## Improving this bot / contact us
We are constantly working on improving this bot in every way. If there is any feedback you would like to give to us or you need some help with the bot, please let us know via a message to the mods of this [Reddit-Community](https://www.reddit.com/r/BADASS_Bot/).

&copy; 2024 Sylvan013 & Anderson4366

[^1]: If these steps do not work: Isch kaputt ... .
