import logging

import click

from .case import cases
from .panels import panels
from .users import users
from .institutes import institutes
from .genes import genes
from .diseases import diseases
from .hpo import hpo
from .whitelist import whitelist
from .aliases import aliases
from .individuals import individuals
from .index import index
from .intervals import intervals
from .collections import collections


LOG = logging.getLogger(__name__)


@click.group()
@click.pass_context
def view(context):
    """
    View objects from the database.
    """
    pass


view.add_command(cases)
view.add_command(panels)
view.add_command(users)
view.add_command(institutes)
view.add_command(genes)
view.add_command(diseases)
view.add_command(hpo)
view.add_command(whitelist)
view.add_command(aliases)
view.add_command(individuals)
view.add_command(index)
view.add_command(intervals)
view.add_command(collections)
