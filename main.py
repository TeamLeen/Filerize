import argparse
import asyncio
import json

import classify
import filetools.fstructs as fstructs
import filetools.ftools as ftools
from classify import FileClassifier
from FileToText import FileToText

labels = {
    'comp1005': 'C Programming',
    'comp1006': 'Assembly',
    'comp1007': 'Digital Logic',
    'comp1001': 'Discrete Maths',
    # 'comp1004': 'Databases',
    # 'comp1043': 'Linear Algebra',
    # 'comp1003': 'Software Engineering',
    # 'comp1009': 'Java and Haskell Programming',
    # 'comp1008': 'Artifitial Intelligence'
}


async def main():
    # debug

    files = ['1001.pdf', '1005.pdf', '1006.pdf', '1007.pdf']
    tasks = {}
    for file in files:
        # PDF to text
        test_pdf: str = FileToText.pdf_to_text(
            f'./test_files/{file}', CUT_STR=True)
        # Classify text
        tasks[file] = asyncio.create_task(
            FileClassifier.classify(test_pdf, labels))

    for file in tasks:
        print(f"Label for {file}: {await tasks[file]}")

asyncio.run(main())
