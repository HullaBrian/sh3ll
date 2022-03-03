from main import CLA


app = CLA("dp>")

@app.command(name="test", callName="test", aliases=["test", "tst"], flags=[], parameters=["e"], help="test command")
def test(**kwargs):
    print("Command 'test' executed.")
    parameters = kwargs["parameters"]

    e = parameters["e"]

    return e 


@app.command(name="add", callName="add", aliases=["add", "a"], flags=[], parameters=["value1", "value2"], help="test2 command")
def add(**kwargs):
    parameters = kwargs["parameters"]
    return int(parameters["value1"]) + int(parameters["value2"])

app.run()