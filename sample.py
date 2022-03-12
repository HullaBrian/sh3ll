from main import CLA


app = CLA("dp>")

@app.command(name="test", callName="test", aliases=["test", "tst"], parameters=["e"], help="test command")
def test(ctx):
    parameters = ctx.parameters

    e = parameters["e"]
    print(e)


@app.command(name="add", callName="add", aliases=["add", "a"], parameters=["v1", "v2"], help="Add command")
def add(ctx):
    parameters = ctx.parameters

    print(int(parameters["v1"]) + int(parameters["v2"]))


app.run()