# sh3ll
sh3ll is a small python package aimed at allowing developers to create simple, yet powerful interactive shell applications.

# Installation
You can install sh3ll from PyPi:

`pip install sh3ll`

Note: only python version 3.0+ is supported.

# How to use sh3ll
sh3ll provides a powerful interface that has many customization options
To use sh3ll, simply use:

`from sh3ll import IS`

From there, create an IS object that will house your commands:

`app = IS(*insert prefix here*)`

After this, you need to create some commands:

```
@app.command(name="", callName="", aliases=["", ""], help="", category="")
def test(ctx):
    print(ctx.parameters)
```

Note: for further information, go to the command categories section

Now that you have commands, you now have to run the app:

`app.run()`

# Features!
sh3ll features a slew of features:
  - Decorator syntax
  - Easy to read code
  - Simple interface
  - Automatic help command generation
  - Command categories

# Command Categories
To use a command inside of a category, all that needs to be done is specify the category name within the command decorator:

`@app.command(name="", callName="", aliases=["", ""], help="", category="")`

and sh3ll will do the rest of the work for you! Now, when trying to call your command you must use the category before you can call the command. This allows for more accurate command names.

Below is an example of a command that has been categorized under the "get" category:

```
@app.command(name="test", callName="test", aliases=["test", "tst"], help="test command", category="get")
def test(ctx):
    print(ctx.parameters)
```

This generates the following in the automatically generated help menu:

```
dp>help
help	Displays this menu

"get" Commands:
---------------
	Command     Aliases            Help            
	-------     --------           ----
	get test    ['test', 'tst']    test command
```

To run this command, simply type in the prompt:

```
dp>get test 1
['1']
```

This runs the command, passing the given parameters to the previosly defined function.

# Application prefixes
To configure the application prefix, simply add the parameter to the creation of the IS object:

`app = IS("prefix>")`

This will be printed after each command to prompt the user for another response.
