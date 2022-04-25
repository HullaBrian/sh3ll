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

`app = IS(prefix=*insert prefix here*, name=*insert name here*)`

Neither of these parameters are required, but are highly recommended

After this, you need to create some commands:

```
@app.command(name="", callName="", aliases=["", ""], help="", category="", progress=(start, end))
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
  - Automatic help command generation (See the "Command Categories" section)
  - Command categories (See the "Command Categories" section)
  - Progress bars (See the "Progress Bars" section for an explanation)

# Command Categories
To use a command inside of a category, all that needs to be done is specify the category name within the command decorator:

`@app.command(name="", callName="", aliases=["", ""], help="", category="", progress=(start, end))`

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

This runs the command, passing the given parameters to the previously defined function.

# Application Prefixes
To configure the application prefix, simply add the parameter to the creation of the IS object:

`app = IS("prefix>")`

This will be printed after each command to prompt the user for another response.

# ASCII Art Initializers
To add ASCII art to initialize the application, simply pass text as a parameter to the IS object as *name*:
```
app = IS(name="App", prefix="dp>")
```
This, when app.run() is called, will print:
```
    _                  
   / \    _ __   _ __  
  / _ \  | '_ \ | '_ \ 
 / ___ \ | |_) || |_) |
/_/   \_\| .__/ | .__/ 
         |_|    |_|    

dp>

```

# Progress Bars
Below is a sample method that implements a progress bar:
```
@app.command(name="prog", help="progress bar tester", progress=(2000, 3000))
def prog(ctx):
    nums = [x * 5 for x in range(2000, 3000)]
    results = []

    for i, x in enumerate(nums):
        results.append(math.factorial(x))
        ctx.progress_bar.progress(1)
```
Within the method header is a progress parameter that contains the start and end point for the progress bar. If you want to start at 0, simply enter (0, *end*) for whatever you need! Once this command is executed, a progress bar will appear, and update every time ctx.progress_bar.progress(*value*) is called. Below is an example of a progress bar being implemented:
```
Progress: |████████████████████████████████████████████████████████████████████████████████████████████████████| 100.00%
```
