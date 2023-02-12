import asyncio
import logging
import os, sys

import click

from config.config import Config
from config import globalvar as gv
import Filerize
from filetools.FileToText import FileToText as fileparser
from listener.filemonitor import ListenForFiles

_common_options = [
    click.argument("directory", type=str),
    
]

_config_options = [
    click.option("--add", type = str, default = None),
    click.option("--delete", type = str, default = None)
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
    if verbose: logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

@cli.command("start", help="run config (on first run), sort, and daemon in order")
@_add_options(_common_options)
@click.help_option("-h", "--help")
@click.pass_context
def cli_start(ctx:click.Context, **args):
    check_directory(args['directory'])
    check_config()
    asyncio.run(Filerize.sort(path=args['directory']))
    # run continous behaviour
    


@cli.command("sort", help="sort all folders in given directory into given labels")
@_add_options(_common_options)
@click.help_option("-h", "--help")
@click.pass_context
def cli_sort(ctx:click.Context, **args):
    check_directory(args['directory'])
    check_config()
    asyncio.run(Filerize.sort(path=args['directory']))
    
@cli.command("listen", help="start a file listen daemon for a given directory")
@_add_options(_common_options)
@click.help_option("-h", "--help")
@click.pass_context
def cli_listen(ctx:click.Context, **args):
    check_directory(args['directory'])
    check_config()
    listener = ListenForFiles(dir=args["directory"])
    listener.run()


@cli.command("config", help="edit config file")
@_add_options(_config_options)
@click.help_option("-h", "--help")
@click.pass_context
def cli_config(ctx:click.Context, **args):
    print("NOT IMPLEMENTED")
    pass

@cli.command("debug", help="debug - not to be in production")
@click.help_option("-h", "--help")
@click.pass_context
def cli_debug(ctx:click.Context, **args):
    Config.load(cfg_path=gv.DEFAULT_CONFIG_PATH)
    label = asyncio.run(Filerize.label_file(r"D:\dev\hacknotts\23\Filerize\testing\untouched\COMP1004-MySQL-setup.docx"))
    print(label)
    pass

@cli.command("recursive_print", help="debug - not to be in production")
@click.help_option("-h", "--help")
@click.pass_context
def cli_debug(ctx:click.Context, **args):
    asyncio.run(Filerize.sort(path=args['directory']))
    pass

    
def check_directory(directory:str = None) -> None:
    if not os.path.exists(directory):
        print("Invalid directory given. Aborting...")
        exit()
    
    



if __name__ == "__main__":
    cli()
