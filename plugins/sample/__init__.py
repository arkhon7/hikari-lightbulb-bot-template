from .plugin import sample_plugin

def load(bot):
	bot.add_plugin(sample_plugin)

def unload(bot):
	bot.remove_plugin(sample_plugin)