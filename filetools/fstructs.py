# sanamorii.github.io
# @sanamorii - jian

import json


class File:
    """ path argument requires \\ \\ not / """
    def __init__(self, path) -> None:
        self.path = path 
        self.name = None
        self.ext = None
        self.hash = None
    
    def parsePath(self) -> None:
        self.name = self.path.split("\\")[-1]
        self.ext = self.path.split(".")[-1]

class Folder:
    def __init__(self, path) -> None:
        self.path = path
        self.files = []  # array of File classes
        self.subfolders = []  # array of Folder classes

    


### debug

# def main():
#     file = File(path=".\\text.txt")
#     file.parsePath()
#     print(file.name, file.ext)
        
# main()