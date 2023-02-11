import argparse
import asyncio
import json
import os

import classify
import filetools.fstructs as fstructs
import filetools.ftools as ftools
from classify import FileClassifier
from config import Config
from FileToText import FileToText


# parser = argparse.ArgumentParser(prog="Filerize",
#                                  description="Document sorter using GPT-3",
#                                  epilog="TEAMLEAN @ NO COPYRIGHT 2023 :^)")
# parser.add_argument("directory", type=str)
# args = parser.parse_args()


async def label_folder(folder: fstructs.Folder):
    files = [file for file in folder.files if file.ext == 'pdf']
    tasks: dict[fstructs.File, asyncio.Task] = {}
    for file in files:
        # PDF to text
        print("SFEFSFESFE: ", file.name)
        test_pdf: str = FileToText.pdf_to_text(
            f'{file.name}', CUT_STR=True, max_output_length=1000)
        # Classify text
        tasks[file] = asyncio.create_task(
            FileClassifier.classify(test_pdf, Config.labels))

    for file in tasks:
        file.label = await tasks[file]


async def main():
    Config.load()
    Config.set_src_folder('test_files')
    folder = fstructs.Folder(path=parsing.args.directory)
    await parsing.RecursiveSearch(folder=folder, visit=label_folder)


asyncio.run(main())
