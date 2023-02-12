import time, sys
import os
import logging
import asyncio

import filetools.fstructs as fstructs
import filetools.ftools as ftools
from classify import FileClassifier
from config.config import Config
from filetools.filemonitor import ListenForFiles
from filetools.FileToText import FileToText
from config import globalvar as gv

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ConfigHandler:
    @staticmethod
    def check_config() -> bool:
        return os.path.exists(gv.DEFAULT_CONFIG_PATH)
        
    @staticmethod   
    def create_config() -> None:
        print("No config file detected...\nInitialising & creating config file...")
        print("Creating config...")
        Config.create(path="config.json")
        print("Input destination directory paths & labels")
        c = 0
        while True:
            pth = sum = None
            
            pth = str(input(f"Enter directory {c+1}: "))
            if not os.path.exists(pth) and pth != "q":
                print("Given directory does not exist")
                continue
            elif pth == "q": break
            
            sum = str(input(f"Enter directory {c+1} summary: "))
            if sum == "q": break
            
            c+=1
            print("\n", end="")
            
            Config.add_label(label=pth, summary=sum)
        if not c:
            # TODO: Delete config file
            print("No directories given. Aborting...")
            exit()
            
        Config.save()
    
    def load_config() -> None:
        Config.load(gv.DEFAULT_CONFIG_PATH)

def init(path) -> fstructs.Folder:
    if not ConfigHandler.check_config():
        ConfigHandler.create_config()
    
    ConfigHandler.load_config()
    
    folder = fstructs.Folder(path = path)
    ftools.full_crawl(folder=folder)
    
    return folder
    
def sort(folder: fstructs.Folder):
    asyncio.run(ftools.label_all(folder=folder))
    ftools.move_all(folder=folder)

def listen(folder: fstructs.Folder):
    ListenForFiles


# async def sort(path: str):
#     folder = fstructs.Folder(path=path)
#     await ftools.recursive_visit(folder=folder, visit=label_files)
#     ftools.recursive_move(folder=folder)


# async def label_files(folder: fstructs.Folder):
#     files = [file for file in folder.files if file.ext == 'pdf']
#     tasks: dict[fstructs.File, asyncio.Task] = {}
#     for file in files:
#         # PDF to text
#         test_pdf: str = FileToText.pdf_to_text(
#             f'{file.path}', CUT_STR=True, max_output_length=1000)
#         # Classify text
#         tasks[file] = asyncio.create_task(
#             FileClassifier.classify(test_pdf, Config.labels))

#     for file in tasks:
#         file.label = await tasks[file]


# async def label_file(path:str):
#     text:str = FileToText.docx_to_text(
#         path=path,
#         CUT_STR=True, max_output_length=1000)
#     return await FileClassifier.classify(text, Config.labels)

if __name__ == "__main__":
    Config.load(cfg_path=gv.DEFAULT_CONFIG_PATH)
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    folder = fstructs.Folder(path=r"D:\dev\hacknotts\23\Filerize\testing\src")
    ftools.full_crawl(folder=folder)
    asyncio.run(ftools.label_all(folder=folder))
    ftools.move_all(folder=folder)
    


