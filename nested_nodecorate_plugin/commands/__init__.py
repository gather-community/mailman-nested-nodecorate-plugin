import click
from mailman.core.i18n import _
from mailman.interfaces.command import ICLISubCommand
from mailman.utilities.options import I18nCommand
from public import public
from zope.interface import implementer

@click.command(
    cls=I18nCommand,
    help=_('Print "Hello!  Bye!" and exit.'))
@click.pass_context
def sayhello(ctx):
    """Say hello and exit."""
    print("Hello!  Bye!")

@public
@implementer(ICLISubCommand)
class SayHello:
    name = 'sayhello'
    command = sayhello
