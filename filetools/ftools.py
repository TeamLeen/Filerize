import asyncio
import json
import os
import logging

from classify import FileClassifier
from filetools.FileToText import FileToText
from config.config import Config

#  local testing
if __name__ == "__main__":
    import fstructs
else:
    import filetools.fstructs as fstructs


def crawl(folder: fstructs.Folder = None) -> fstructs.Folder:
    """ crawl first level of given directory """
    root = folder.path

    for item in os.listdir(root):
        path = os.path.join(root, item)

        if os.path.isfile(path=path):
            file = fstructs.File(path=path)
            folder.files.append(file)
        else:
            subfolder = fstructs.Folder(path=path)
            folder.subfolders.append(subfolder)

    return folder

def full_crawl(folder: fstructs.Folder = None) -> None:
    """
    Crawl entire structure and return directory tree of given root directory - Done recursively
    """
    folder = crawl(folder=folder)
    for subfolder in folder.subfolders: full_crawl(folder=subfolder)
    


async def label_all(folder: fstructs.Folder = None):
    """ 
    Parent Function
    
    Give all included files found in tree a label according to GPT-3
    """
    await label_files(folder=folder)
    for subfolder in folder.subfolders: await label_all(folder=subfolder)

async def label_files(folder: fstructs.Folder):
    """
    Child Function to label_all
    
    Parse documents and classify them w/ labels provided by config 
    """
    
    # TODO: allow multiple document types
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

async def label_file(path:str):
    """
    Child function to FileMonitor
    
    Parse single document and classify with label
    """
    text:str = FileToText.docx_to_text(
        path=path,
        CUT_STR=True, max_output_length=1000)
    return await FileClassifier.classify(text, Config.labels)



def print_tree(folder: fstructs.Folder = None):
    """
    Debug -> print tree recursively
    """
    for file in folder.files: print(file.path, file.name)
    for subfolder in folder.subfolders:
        print(f"moving to {subfolder.path}")
        print_tree(folder = subfolder)

def move_all(folder: fstructs.Folder = None) -> None:
    """
    Move all files found in given tree to assigned label in File object recursively
    """
    for file in folder.files:
        move_single(src=file.path, dst_root=file.label, filename=file.name)
            
    for subfolder in folder.subfolders:
        move_all(folder=subfolder)



def move_single(src: str, dst_root: str, filename: str) -> None:
    """ move file """
    print(dst_root, src)
    if dst_root and os.path.exists(src):
        dst = os.path.abspath(os.path.join(dst_root, filename))
        os.rename(src=src, dst=dst)
    else:
        logging.info(f"skipped")
