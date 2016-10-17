import click

from .chorao_ipsum import ChoraoIpsum


@click.command()
@click.option('--count', default=100, help='Number of Choratims.')
def cli_chorao_ipsum(count):
    click.echo(ChoraoIpsum(count).get_text())


def main():
    cli_chorao_ipsum()
