from main import CLA


app = CLA("dp>")


@app.command(name="test", callName="test", aliases=["test", "tst"], help="test command", category="get")
def test(ctx):
    print(ctx.parameters)


@app.command(name="add", callName="add", aliases=["add", "a"], help="Add command", category="operator")
def add(ctx):
    print(int(ctx.parameters[0]) + int(ctx.parameters[1]))


@app.command(name="multiply", callName="multiply", aliases=["m", "multi"], help="Multiply command", category="operator")
def multiply(ctx):
    print(ctx.parameters)
    print("M:", int(ctx.parameters[0]) * int(ctx.parameters[1]))


app.run()