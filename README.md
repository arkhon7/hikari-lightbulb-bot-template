# HIKARI-LIGHTBULB-TEMPLATE

A simple template for your hikari-lightbulb bot project.

### Running the bot

You can run the bot by executing `main.py` file

### Folder structure
```Python
.
├── plugins/
│   ├── foobar/
│   │   ├── __init__.py
│   │   ├── plugin.py ------- main file of the plugin
│   │   ├── foo.py 
│   │   ├── bar.json
│   │   └── baz.txt
│   └── __init__.py
└── main.py ----------------- execute this file to run bot
```

### Creating plugins

This template comes with a simple script `create_plugin.py` that creates a template plugin into the **plugins** folder
To create plugin, run

```Python
python.exe -m create_plugin <name of your plugin>
```
