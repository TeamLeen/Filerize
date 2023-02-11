import argparse
import click
import os

import filetools.fstructs as fstructs
import filetools.ftools as ftools
from listen.filelistener import ListenForFiles


parser = argparse.ArgumentParser(prog="Filerize", 
                                 description="Document sorter using GPT-3",
                                 epilog="TEAMLEAN @ NO COPYRIGHT 2023 :^)")
parser.add_argument("directory", type=str)
args = parser.parse_args()

def main():
    folder = fstructs.Folder(path = args.directory)
    RecursiveSearch(folder = folder)

    listener = ListenForFiles()
    listener.run()


def RecursiveSearch(folder: str = None):
    folder = ftools.crawl(folder=folder)

    for i in range(0, len(folder.files)):

        # do classification here
        print(folder.files[i].name)

    for j in range(0, len(folder.subfolders)):
        RecursiveSearch(folder = folder.subfolders[j])



main()