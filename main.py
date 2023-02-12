import argparse
import asyncio
import logging
import os
import sys

import api
from config import Config

parser = argparse.ArgumentParser(prog="Filerize",
                                 description="Document sorter using GPT-3",
                                 epilog="TEAMLEAN @ NO COPYRIGHT 2023 :^)")
parser.add_argument("directory", type=str)
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()


def main():
    if args.verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    if os.path.exists('config.json'):
        Config.load('config.json')
    elif os.path.exists('config.example.json'):  # fallback
        Config.load('config.example.json')
    else:
        print("No config file detected...\nInitialising & creating config file...")
        print("Input destination directory paths & labels")
        c = 0
        while True:
            pth = sum = None
            
            pth = str(input(f"Enter directory {c+1}: "))
            if not os.path.exists(pth) and pth != "q":
                print("Given directory does not exist")
                continue
            elif pth == "q":
                break
            
            sum = str(input(f"Enter directory {c+1} summary: "))
            if sum == "q":
                break
            
            c+=1
            print("\n", end="")
            
        
            # Config.add_label(label=pth, summary=sum)
        print("Creating config...")
    

    asyncio.run(api.init(args))


if __name__ == "__main__":
    main()
