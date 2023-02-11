import os
import json

import fstructs

# def crawl(dir:str = None):
#     for root, dirs, files in os.walk(dir):
#         for folder in dirs:
#             path = os.path.join(root, folder) + "\\"
#             print(folder)

def crawl(folder:fstructs.Folder = None):

    fileCount = 0
    folderCount = 0

    root = folder.path

    for item in os.listdir(root):
        path = os.path.join(root, item)


        if os.path.isfile(path=path):

            file = fstructs.File(path = path)
            file.parsePath()

            folder.files.append(file)
            fileCount += 1
        else:
            subfolder = fstructs.Folder(path=path)
            folder.subfolders.append(subfolder)
            folderCount += 1
    
    return folder, (fileCount, folderCount)

def main():
    folder = fstructs.Folder(path="D:\\music")
    cfolder, count = crawl(folder=folder)
    for f in cfolder.subfolders:
        print(f.path)

main()