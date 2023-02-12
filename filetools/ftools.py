import asyncio
import json
import os
import logging

#  local testing
if __name__ == "__main__":
    import fstructs
else:
    import filetools.fstructs as fstructs


def crawl(folder: fstructs.Folder = None) -> fstructs.Folder:
    """ crawl first level of given directory """

    root = folder.path

    for item in os.listdir(root):
        path = os.path.join(root, item)

        if os.path.isfile(path=path):
            file = fstructs.File(path=path)
            folder.files.append(file)
        else:
            subfolder = fstructs.Folder(path=path)
            folder.subfolders.append(subfolder)

    return folder

async def recursive_visit(folder: fstructs.Folder = None, visit=None):
    folder = crawl(folder=folder)

    if visit is not None:
        await visit(folder)

    for subfolder in folder.subfolders:
        await recursive_visit(folder=subfolder, visit=visit)

def recursive_move(folder: fstructs.Folder = None) -> None:

    for file in folder.files:
        move(src=file)
            
    for subfolder in folder.subfolders:
        recursive_move(folder=subfolder)

def recursive_print(folder: fstructs.Folder = None):
    for file in folder.files:
        print(file.path, file.name)
    for subfolder in folder.subfolders:
        print(f"moving to {subfolder.path}")
        recursive_print(folder = subfolder)

def move(src: fstructs.File = None) -> None:
    """ move file """

    if src.label and os.path.exists(src.path):
        dst = os.path.abspath(os.path.join(src.label, src.name))
        os.rename(src=src.path, dst=dst)
    else:
        logging.error(f"failed")
