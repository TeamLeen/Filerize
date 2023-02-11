import os
import json

import filetools.fstructs as fstructs
import filetools.ftools as ftools

def main():
    ## debug
    folder = fstructs.Folder(path = "D:\\music")

    folder, count = ftools.crawl(folder = folder)

    for dir in folder.subfolders:
        print(dir.path)

main()