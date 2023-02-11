import os
import json

#  local testing
if __name__ == "__main__":
    import fstructs
else:
    import filetools.fstructs as fstructs


def crawl(folder:fstructs.Folder = None):

    fileCount = 0
    folderCount = 0

    root = folder.path

    for item in os.listdir(root):
        path = os.path.join(root, item)


        if os.path.isfile(path=path):

            file = fstructs.File(path = path)

            folder.files.append(file)
            fileCount += 1
        else:
            subfolder = fstructs.Folder(path=path)
            folder.subfolders.append(subfolder)
            folderCount += 1
    
    return folder, (fileCount, folderCount)


def move(src: fstructs.File = None, dst: str = None):
    """ UHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh """

    srcPath = src.path
    dstPath = os.path.join(dst, src.name)

    if os.path.exists(srcPath):
        os.rename(src = src.path, dst = dstPath)
    else:
        raise FileNotFoundError





##debug
# def main():
#     file = fstructs.File(path=r"D:\dev\hacknotts\23\Filerize\filetools\example_file.txt")
#     move(src=file, dst=r"D:\dev\hacknotts\23\Filerize\filetools\dst")

# main()