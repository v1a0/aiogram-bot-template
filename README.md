# Template structure

```shell
aiogram-bot-template
|   .gitattributes
|   .gitignore
|   autorun.py      # infinite loop run bot.py (restart if bot fail)
|   bot.py          # main file, dp.executor.start_polling, from handlers import *
|   branches.py     # State's init as branches
|   LICENSE         # just license
|   messages.py     # Dict with text messages MSG['hello']
|   misc.py         # Bot init, Dispatcher init
|   settings.py     # API_TOKEN, ADMIN_ID, BAN_LIST, DB_PATH, logger settings
|
\---handlers            # dp.handlers
    |   start.py        # template handler for /start and /indo
    |   text_message.py # template handlers for TEXT-messages
```