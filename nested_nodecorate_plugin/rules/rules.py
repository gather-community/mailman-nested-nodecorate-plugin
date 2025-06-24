from mailman.interfaces.rules import IRule
from public import public
from zope.interface import implementer

# Documentation for rules:
# https://docs.mailman3.org/projects/mailman/en/latest/src/mailman/rules/docs/rules.html

# Each rule implements the IRule interface:
# https://gitlab.com/mailman/mailman/-/blob/master/src/mailman/interfaces/rules.py
@public
@implementer(IRule)
class ExampleRule:

    # A unique name for the new rule.
    name = 'example-rule'

    # Some brief description for the rule.
    description = 'An example rule.'

    # Should this rule's success or failure be recorded?
    # This is a boolean; if True then this rule's hit or miss will be
    # recorded in a message header.  If False, it won't.
    record = True

    def check(self, mlist, msg, msgdata):
        return 'example' in msgdata
