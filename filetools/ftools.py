import asyncio
import json
import os
import shutil

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


def recursive_move(folder: fstructs.Folder = None) -> None:
    folder = crawl(folder=folder)

    for file in folder.files:
        copy(src=file)
        
    for subfolder in folder.subfolders:
        recursive_move(folder=subfolder)


async def recursive_visit(folder: fstructs.Folder = None, visit=None):
    folder = crawl(folder=folder)

    if visit is not None:
        await visit(folder)

    for subfolder in folder.subfolders:
        await recursive_visit(folder=subfolder, visit=visit)


def move(src: fstructs.File = None, dst: str = None) -> None:
    """ move folder """

    srcPath = src.path
    dstPath = os.path.join(dst, src.name)

    if os.path.exists(srcPath):
        os.rename(src=src.path, dst=dstPath)
    else:
        raise FileNotFoundError
    
def copy(src: fstructs.File = None) -> None:
    """ copy file """

    if os.path.exists(src.path):
        dst = os.path.join(src.label, src.name)
        os.rename(src=src.path, dst=dst)
    else:
        raise FileNotFoundError
    

# debug
# def main():
#     file = fstructs.File(path=r"D:\dev\hacknotts\23\Filerize\filetools\example_file.txt")
#     move(src=file, dst=r"D:\dev\hacknotts\23\Filerize\filetools\dst")

# main()
