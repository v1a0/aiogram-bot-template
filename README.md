# Template structure
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fv1a0%2Faiogram-bot-template.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fv1a0%2Faiogram-bot-template?ref=badge_shield)


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

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fv1a0%2Faiogram-bot-template.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fv1a0%2Faiogram-bot-template?ref=badge_large)