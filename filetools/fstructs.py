# sanamorii.github.io
# @sanamorii - jian

import json
from hashlib import sha256

class File(object):
    """ path argument requires \\ \\ not / """
    def __init__(self, path) -> None:
        self.path = path 
        self.name, self.ext = self.ParsePath()
        self.hash = self.Hash()

        
        
    
    def ParsePath(self) -> None:
        return self.path.split("\\")[-1], self.path.split(".")[-1]

    def Hash(self):
        BUF_SIZE = 65536
        hash = sha256()
        with open(self.path, "rb") as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                hash.update(data)
        return hash
        

class Folder(object):
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