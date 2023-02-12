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
        # self.hash = self.Hash()
        self.label: str | None = None

    def ParsePath(self) -> tuple[str, str]:
        filename = os.path.basename(self.path)
        if "." in filename: ext = filename.split(".")[-1]
        else: ext = None
        
        # print(filename, ext)
        return os.path.basename(self.path), ext

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


class Folder(object):
    def __init__(self, path) -> None:
        self.path = path
        self.files: list[File] = []  # array of File classes
        self.subfolders: list[Folder] = []  # array of Folder classes
