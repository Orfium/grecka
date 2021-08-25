import click

from grecka.convert import Grecka


@click.group()
def test():
    pass


@test.command()
@click.argument("sentence", type=click.STRING)
def to_greeklish(sentence: str):
    click.echo(Grecka.toGreeklish(sentence))


if __name__ == "__main__":
    test()
