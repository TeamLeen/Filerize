import argparse
import click
import os

import filetools.fstructs as fstructs
import filetools.ftools as ftools
import config.setconfig as setconfig


parser = argparse.ArgumentParser(prog="Filerize", 
                                 description="Document sorter using GPT-3",
                                 epilog="TEAMLEAN @ NO COPYRIGHT 2023 :^)")
parser.add_argument("directory", type=str)
parser.add_argument("-s", "--setup", action="store_true")
args = parser.parse_args()


def cli():
    pass


def main():
    if args.setup:
        setconfig.InitConfig()
    else:
        folder = fstructs.Folder(path = args.directory)
        RecursiveSearch(folder = folder)

def RecursiveSearch(folder: str = None):
    folder = ftools.crawl(folder=folder)

    for i in range(0, len(folder.files)):

        # do classification here

        ftools.move()
        print(folder.files[i].name.encode('ascii', 'ignore'))

    for j in range(0, len(folder.subfolders)):
        print(f"\n====\nJumping folders -> {folder.subfolders[j].path.encode('ascii', 'ignore')}\n====\n")
        RecursiveSearch(folder = folder.subfolders[j])
    print(f"\n --- complete one ---> {folder.path.encode('ascii', 'ignore')}")

main()