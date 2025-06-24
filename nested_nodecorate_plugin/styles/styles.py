from public import public
from mailman.interfaces.styles import IStyle
from mailman.styles.default import LegacyDefaultStyle
from zope.interface import implementer

# Documentation on List styles
# https://docs.mailman3.org/projects/mailman/en/latest/src/mailman/styles/docs/styles.html

@public
@implementer(IStyle)
class MyPrivateStyle(LegacyDefaultStyle):

    # Provide a unique name to this style so it doesn't clash with the ones
    # defined by default.
    name = 'plugin-style'

    # Provide a usable description that will be shown to the users in Web
    # Interface.
    description = 'Ordinary discussion mailing list style.'

    def apply(self, mailing_list):
        """See `IStyle`."""
        # Set settings from super class.
        super().apply(mailing_list)

        # Make modifications on top.
        mlist.display_name = 'My Private Style'
