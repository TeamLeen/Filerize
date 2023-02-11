import argparse
import asyncio
import json
import os
import sys
import threading
import logging


import classify
import filetools.fstructs as fstructs
import filetools.ftools as ftools
from listener.filemonitor import ListenForFiles
from classify import FileClassifier
from config import Config
from filetools.FileToText import FileToText

parser = argparse.ArgumentParser(prog="Filerize",
                                 description="Document sorter using GPT-3",
                                 epilog="TEAMLEAN @ NO COPYRIGHT 2023 :^)")
parser.add_argument("directory", type=str)
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

if args.verbose: logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def listen_daemon():
    listen = ListenForFiles(r"D:\dev\hacknotts\23\Filerize\test_files")
    listen.run()

async def label_folder(folder: fstructs.Folder):
    files = [file for file in folder.files if file.ext == 'pdf']
    tasks: dict[fstructs.File, asyncio.Task] = {}
    for file in files:
        # PDF to text
        test_pdf: str = FileToText.pdf_to_text(
            f'{file.path}', CUT_STR=True, max_output_length=1000)
        # Classify text
        tasks[file] = asyncio.create_task(
            FileClassifier.classify(test_pdf, Config.labels))

    for file in tasks:
        file.label = await tasks[file]


async def main():
    print("test")
    Config.load()
    Config.set_src_folder('test_files')
    folder = fstructs.Folder(path=args.directory)
    await ftools.recursive_visit(folder=folder, visit=label_folder)

    for i in range(0, len(folder.subfolders)):
        print(f"{folder.subfolders[i]}")


asyncio.run(main())
