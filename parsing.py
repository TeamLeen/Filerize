import argparse
import asyncio

import filetools.fstructs as fstructs
import filetools.ftools as ftools
from listen.filelistener import ListenForFiles

parser = argparse.ArgumentParser(prog="Filerize",
                                 description="Document sorter using GPT-3",
                                 epilog="TEAMLEAN @ NO COPYRIGHT 2023 :^)")
parser.add_argument("directory", type=str)
args = parser.parse_args()