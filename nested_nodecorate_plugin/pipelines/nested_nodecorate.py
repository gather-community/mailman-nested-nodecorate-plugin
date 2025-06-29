# Copyright (C) 2006-2023 by the Free Software Foundation, Inc.
#
# This file is part of GNU Mailman.
#
# GNU Mailman is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# GNU Mailman is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# GNU Mailman.  If not, see <https://www.gnu.org/licenses/>.

"""Avoid Decorating messages in nested list."""

from mailman.core.i18n import _
from mailman.pipelines.base import BasePipeline
from public import public


@public
class NestedNodecoratePipeline(BasePipeline):
    """The built-in posting pipeline."""

    name = 'nested-nodecorate-pipeline'
    description = _('Avoid decorating messages to nested lists')

    _default_handlers = (
        'validate-authenticity',
        'mime-delete',
        'tagger',
        'member-recipients',
        'avoid-duplicates',
        'cleanse',
        'cleanse-dkim',
#        'suppress-decoration',
        'cook-headers',
        'nested-subject-prefix',
        'rfc-2369',
        'to-archive',
        'to-digest',
        'to-usenet',
        'after-delivery',
        'acknowledge',
        # All decoration is now done in delivery.
        # 'decorate',
        'nested-dmarc',
        # Message decoration in delivery can break an arc signature, so sign
        # in delivery after decorating.
        # 'arc-sign',
        'to-outgoing',
        )
