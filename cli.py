from typer import Typer
from interfaces.cli.modules import taxes

app = Typer()
app.add_typer(typer_instance=taxes.app, name="taxes")


if __name__ == "__main__":
    app()
