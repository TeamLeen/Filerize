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


# def main():
#     folder = fstructs.Folder(path=args.directory)
#     RecursiveSearch(folder=folder)


async def RecursiveSearch(folder: fstructs.Folder = None, visit=None):
    folder = ftools.crawl(folder=folder)

    asyncio.create_task(visit(folder))

    for file in folder.files:
        # ftools.move()
        print(file.name)

    for subfolder in folder.subfolders:
        print(
            f"\n====\nJumping folders -> {subfolder.path}\n====\n")
        await RecursiveSearch(folder=subfolder, visit=visit)
    print(f"\n --- complete one ---> {folder.path}")


# main()
