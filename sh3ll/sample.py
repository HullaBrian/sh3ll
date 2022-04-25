import math

from sh3ll import IS


app = IS(name="Depth-Finder", prefix="dp>")


@app.command(name="test", aliases=["test", "tst"], help="test command")
def test(ctx):
    print(ctx.parameters)


@app.command(name="add", aliases=["add", "a"], help="Add command", category="operator")
def add(ctx):
    print(int(ctx.parameters[0]) + int(ctx.parameters[1]))


@app.command(name="multiply", aliases=["m", "multi"], help="Multiply command", category="operator")
def multiply(ctx):
    print(ctx.parameters)
    print("M:", int(ctx.parameters[0]) * int(ctx.parameters[1]))


@app.command(name="prog", help="progress bar tester", progress=(2000, 3000))
def prog(ctx):
    nums = [x * 5 for x in range(2000, 3000)]
    results = []

    for i, x in enumerate(nums):
        results.append(math.factorial(x))
        ctx.progress_bar.progress(1)


app.run()
