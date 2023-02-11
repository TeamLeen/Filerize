import json
import os

import classify
import filetools.fstructs as fstructs
import filetools.ftools as ftools
from FileToText import FileToText

labels = {
    'comp1005': 'C',
    'comp1006': 'Assembly',
    'comp1007': 'Digital Logic',
    'comp1001': 'Discrete Maths',
    # 'comp1004': 'Databases',
    # 'comp1043': 'Linear Algebra',
    # 'comp1003': 'Software Engineering',
    # 'comp1009': 'Java and Haskell Programming',
    # 'comp1008': 'Artifitial Intelligence'
}


def main():
    # debug
    # folder = fstructs.Folder(path="D:\\music")

    # folder, count = ftools.crawl(folder=folder)

    # for dir in folder.subfolders:
    #     print(dir.path)

    # PDF to text
    test_pdf: str = FileToText.pdf_to_text(
        './test_files/1007_cw.pdf', CUT_STR=True)
    # Classify text
    print(f"Label for test pdf: {classify.classify(test_pdf, labels)}")


main()
