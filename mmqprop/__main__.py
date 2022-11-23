from . import version
from .cli import cli

if __name__ == '__main__':
    print("mmqprop version:", version())
    cli()
