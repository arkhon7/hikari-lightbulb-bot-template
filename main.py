import lightbulb
import logging
from plugins import PLUGINS

logging.basicConfig(level=logging.DEBUG)


# Run your bot here!
def build_bot(TOKEN):
    bot = lightbulb.BotApp(TOKEN)
    for plugin in PLUGINS:
        try:
            bot.load_extensions(f"plugins.{plugin}")
        except lightbulb.ExtensionMissingLoad:
            pass

    return bot


TOKEN = "Your bot token"
bot = build_bot(TOKEN)

bot.run()
