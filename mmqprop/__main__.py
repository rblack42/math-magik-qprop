import click

from . import version
from .cli import cli
import sys


@click.command()
@click.option('--single', 'runtype', flag_value='single', show_default=True)
@click.option('--interactive', 'runtype', flag_value='interactive', show_default=True)
@click.option('--debug/--no-debug', default=False, help="Run in foreground")
def gui(runtype, debug):
    click.echo(runtype)
    if runtype == 'interactive':
        cli(debug)
    else:
        print("runtype: single", debug)


if __name__ == "__main__":
    print("mmqprop version:", version())
    gui()
