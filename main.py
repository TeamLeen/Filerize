import json
import argparse

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


<<<<<<< HEAD
parser = argparse.ArgumentParser(prog="Filerize", 
                                 description="Document sorter using GPT-3",
                                 epilog="TEAMLEAN @ NO COPYRIGHT 2023 :^)")
parser.add_argument("directory", type=str)
args = parser.parse_args()

def parsing():
    folder = fstructs.Folder(path = args.directory)
    folder, count = ftools.crawl(folder=folder)
=======
def main():
    # debug
    # folder = fstructs.Folder(path="D:\\music")

    # folder, count = ftools.crawl(folder=folder)
>>>>>>> 5248b805e814b60d30cf6ce72f77aab2a72174f5

    # for dir in folder.subfolders:
    #     print(dir.path)

def main():
    ## debug

    # PDF to text
    test_pdf: str = FileToText.pdf_to_text(
        './test_files/1007_cw.pdf', CUT_STR=True)
    # Classify text
    print(f"Label for test pdf: {classify.classify(test_pdf, labels)}")


main()
