# sanamorii.github.io
# @sanamorii - jian

import json
import os
from hashlib import sha256


class File(object):
    """ path argument requires \\ \\ not / """

    def __init__(self, path) -> None:
        self.path: str = path
        self.name, self.ext = self.ParsePath()

        self.label = None
        # self.hash = self.Hash()
<<<<<<< HEAD
        # self.hash = None

=======
        self.hash = None
        self.label: str | None = None
>>>>>>> 5492d6928ea2a2a3b4574a27d7234f824a68c0b6

    def ParsePath(self) -> tuple[str, str]:
        return self.path.split("\\")[-1], self.path.split(".")[-1]

<<<<<<< HEAD
    def set_label(self, label) -> None:
        self.label = label

    # def Hash(self):
    #     BUF_SIZE = 65536
    #     hash = sha256()
    #     with open(self.path, "rb") as f:
    #         while True:
    #             data = f.read(BUF_SIZE)
    #             if not data:
    #                 break
    #             hash.update(data)
    #     return hash
        
=======
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

>>>>>>> 5492d6928ea2a2a3b4574a27d7234f824a68c0b6

class Folder(object):
    def __init__(self, path) -> None:
        self.path = path
        self.files: list[File] = []  # array of File classes
        self.subfolders: list[Folder] = []  # array of Folder classes
