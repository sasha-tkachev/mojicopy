import typer

app = typer.Typer()


@app.command()
def main():
    typer.echo("Hello World")


if __name__ == "__main__":
    app()
