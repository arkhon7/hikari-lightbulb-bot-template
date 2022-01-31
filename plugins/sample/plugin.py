import lightbulb

# plugin instances
sample_plugin = lightbulb.Plugin("sample_plugin")

# your hikari bot plugin code here!
# You can change the command below
@sample_plugin.command
@lightbulb.command(name="sample", description="your command description here")
@lightbulb.implements(lightbulb.SlashCommand)
async def _sample_hello_world(ctx: lightbulb.Context):
	await ctx.respond("Hello, World!")