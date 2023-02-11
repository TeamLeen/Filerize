import argparse
import os

import filetools.fstructs as fstructs
import filetools.ftools as ftools


parser = argparse.ArgumentParser(prog="Filerize", 
                                 description="Document sorter using GPT-3",
                                 epilog="TEAMLEAN @ NO COPYRIGHT 2023 :^)")
parser.add_argument("directory", type=str)
args = parser.parse_args()

def main():
    folder = fstructs.Folder(path = args.directory)
    folder, count = ftools.crawl(folder=folder)

    for dir in folder.subfolders:
        print(dir.path)
    for file in folder.files:
        print(file.path)

main()