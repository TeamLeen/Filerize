import asyncio
import logging
import os
import sys
import threading

import click

import Filerize
from config import globalvar as gv
from config.config import Config
from filetools.FileToText import FileToText as fileparser
from filetools.fwatchdog import ListenForFiles

_common_options = [
    click.argument("directory", type=str),

]

_config_options = [
    click.option("--add", type=str, default=None),
    click.option("--delete", type=str, default=None),
    click.option("--show", default=None, count=True)
]


def _add_options(opts: list):
    def wrap(func):
        for opt in opts:
            func = opt(func)
        return func

    return wrap


@click.group()
@click.option("-v", "--verbose", default=None, count=True)
def cli(verbose):
    """FilerizeCLI @ TeamLEAN - A Document Sorter using GPT-3"""
    if verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


@cli.command("start", help="run config (on first run), sort, and daemon in order")
@_add_options(_common_options)
@click.help_option("-h", "--help")
@click.pass_context
def cli_start(ctx: click.Context, **args):
    check_directory(directory=args['directory'])
    folder = Filerize.init(args['directory'])
    Filerize.sort(folder=folder)

    Filerize.listen(folder=folder)
    # run continous behaviour


@cli.command("sort", help="sort all folders in given directory into given labels")
@_add_options(_common_options)
@click.help_option("-h", "--help")
@click.pass_context
def cli_sort(ctx: click.Context, **args):
    check_directory(directory=args['directory'])
    folder = Filerize.init(args['directory'])
    Filerize.sort(folder=folder)


@cli.command("listen", help="start a file listen daemon for a given directory")
@_add_options(_common_options)
@click.help_option("-h", "--help")
@click.pass_context
def cli_listen(ctx: click.Context, **args):
    check_directory(directory=args['directory'])
    folder = Filerize.init(args['directory'])
    Filerize.listen(folder=folder)


@cli.command("config", help="edit config file")
@_add_options(_config_options)
@click.help_option("-h", "--help")
@click.pass_context
def cli_config(ctx: click.Context, **args):

    if all([args["add"], args["delete"], args["show"]]):
        print("usage: --add | --delete | --show | (not all)")
        return
    else:
        Config.load(gv.DEFAULT_CONFIG_PATH)

    if args['add']:

        pth = os.path.abspath(args["add"])

        if not os.path.exists(path=pth):
            print("Warning: Path does not exist. Making one...")
            os.mkdir(pth)
        sum = str(input(f"Enter directory summary: "))
        if sum == "":
            print("Error: no summary. Aborting...")
            return
        Config.add_label(label=pth, summary=sum)
        Config.save()

    elif args["delete"]:
        pth = os.path.abspath(args["delete"])
        stat = Config.delete_label(label=pth)
        if stat:
            print("Entry Deleted")
        else:
            print("Error: entry does not exist")

        Config.save()

    elif args["show"]:
        Config.print_config()


# @cli.command("debug", help="debug - not to be in production")
# @click.help_option("-h", "--help")
# @click.pass_context
# def cli_debug(ctx:click.Context, **args):
#     Config.load(cfg_path=gv.DEFAULT_CONFIG_PATH)
#     label = asyncio.run(Filerize.label_file(r"D:\dev\hacknotts\23\Filerize\testing\untouched\COMP1004-MySQL-setup.docx"))
#     print(label)
#     pass

# @cli.command("recursive_print", help="debug - not to be in production")
# @click.help_option("-h", "--help")
# @click.pass_context
# def cli_debug(ctx:click.Context, **args):
#     asyncio.run(Filerize.sort(path=args['directory']))
#     pass


def check_directory(directory: str) -> None:
    if not os.path.exists(directory):
        print("Invalid directory given. Aborting...")
        exit()


if __name__ == "__main__":
    cli()
