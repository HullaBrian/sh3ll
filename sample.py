from main import CLA


app = CLA("dp>")

@app.command(name="test", callName="test", aliases=["test", "tst"], help="test command")
def test(ctx):
    print(ctx.parameters)


@app.command(name="add", callName="add", aliases=["add", "a"], help="Add command")
def add(ctx):
    print(int(ctx.parameters[0]) + int(ctx.parameters[1]))


app.run()