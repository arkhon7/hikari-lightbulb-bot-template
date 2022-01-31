"""
This is a simple utility script of the template, it allows you to
create template plugins into plugins folder 
"""
import os
import sys


def create_plugin(name: str):
    plugin_path = f"plugins/{name}"
    if not os.path.isdir(plugin_path):
        os.makedirs(plugin_path)

    with open(f"plugins/{name}/__init__.py", "w") as init:
        content = (
            f"from .plugin import {name}_plugin\n\n"
            f"def load(bot):\n\tbot.add_plugin({name}_plugin)\n\n"
            f"def unload(bot):\n\tbot.remove_plugin({name}_plugin)"
        )

        init.write(content)

    with open(f"plugins/{name}/plugin.py", "w") as plugin:
        content = (
            "import lightbulb\n\n"
            f'# plugin instances\n{name}_plugin = lightbulb.Plugin("{name}_plugin")\n\n'
            "# your hikari bot plugin code here!\n"
            f"# You can change the command below\n@{name}_plugin.command\n"
            f'@lightbulb.command(name="{name}", description="your command description here")\n'
            "@lightbulb.implements(lightbulb.SlashCommand)\n"
            f"async def _{name}_hello_world(ctx: lightbulb.Context):\n\t"
            'await ctx.respond("Hello, World!")'
        )
        plugin.write(content)

    print(f"created {name} plugin")


create_plugin(sys.argv[1])
