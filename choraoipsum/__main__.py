import click

from . import ChoraoIpsum


@click.command()
@click.option('--count', default=100, help='Number of Choratims.')
def main(count):
    click.echo(ChoraoIpsum(count).get_text())


# Call application
main()
