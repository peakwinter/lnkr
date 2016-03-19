# -*- coding: utf-8 -*-
from __future__ import print_function

import click

from lnkr import create_app
from lnkr.models import Shortlink
from lnkr.database import init_db, session


@click.group()
def main():
    pass

@click.command()
def run():
    """
    Run internal API server
    """
    app = create_app()
    app.run(host="0.0.0.0")

@click.argument("url")
@click.command()
def add(url):
    """
    Manually add a shortlink from the command line
    """
    init_db()
    link = Shortlink(url)
    session.add(link)
    session.commit()

    newlink = click.style("http://<yoururl>/go/{}".format(link.id), bold=True)
    click.echo("Poof! Your link is now shortened to: " + newlink)


main.add_command(run)
main.add_command(add)
