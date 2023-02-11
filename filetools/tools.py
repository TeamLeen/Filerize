import os
import json

# def crawl(dir:str = None):
#     for root, dirs, files in os.walk(dir):
#         for folder in dirs:
#             path = os.path.join(root, folder) + "\\"
#             print(folder)

def crawl(root:str = None):
    for item in os.listdir(root):
        print(item)

def main():
    crawl(root="D:\\music")

main()