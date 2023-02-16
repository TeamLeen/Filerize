import json
import os

from config import globalvar as gv
from filetools import fstructs

template = {
    "folders": [],
}


class Config:
    path: str = gv.DEFAULT_CONFIG_PATH
    src_dir: str = None
    folder: fstructs.Folder = None
    labels = {}

    @classmethod
    def load(cls, cfg_path) -> None:
        cls.path = os.path.abspath(cfg_path)

        with open(file=cls.path, encoding="utf-8", mode="r") as f:
            parsed = json.load(f)

            # cls.src_folder_path = os.path.abspath(parsed['src_folder_path'])

            # Convert list of kv pairs to dict
            for folder in parsed['folders']:
                cls.labels[folder['path']] = folder['summary']

    @classmethod
    def save(cls) -> None:
        # Convert dict to list of kv pairs
        buffer = {}
        # buffer['src_folder_path'] = os.path.abspath(
        #     cls.src_folder_path)  # redunant but might as well

        buffer['folders'] = []
        for label in cls.labels:
            buffer['folders'].append({
                'path': label,
                'summary': cls.labels[label]
            })

        with open(file=cls.path, encoding='utf-8', mode="w") as f:
            json.dump(buffer, f)

    # TODO: create config file if not exist
    @classmethod
    def create(cls, path: str = None) -> None:
        cls.path = os.path.abspath(path=path)
        with open(file=cls.path, mode="w+") as f:
            json_obj = json.dumps(template, indent=4)
            f.write(json_obj)

    # TODO: delete config file - related to cli.py
    # def delete(cls, path:str = None) -> None:

    @classmethod
    def add_label(cls, label: str, summary: str) -> None:
        cls.labels[label] = summary

    @classmethod
    def delete_label(cls, label: str) -> bool:
        if label in cls.labels:
            del cls.labels[label]
            return True
        return False

    @classmethod
    def set_src_dir(cls, path) -> None:
        cls.src_dir = path

    @classmethod
    def set_folder(cls, folder: fstructs.Folder) -> None:
        cls.folder = folder

    @classmethod
    def print_config(cls):
        for key, value in cls.labels.items():
            print("{:<32} | {:<32}".format(
                f"Path: {key}", f"Summary: {value}"))


# if __name__ == '__main__':
#     Config.load()
#     Config.set_src_folder('test_files')

#     # Debug print
#     print(Config.labels)
#     print(Config.src_folder_path)
