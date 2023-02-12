import json
import os

template = {
    "folders": [],
}

DEFAULT_CONFIG_PATH = 'config.json'
DEFAULT_SOURCE_FOLDER = '.'


class Config:
    path: str = DEFAULT_CONFIG_PATH
    labels = {}

    @classmethod
    def load(cls, cfg_path) -> None:
        cls.path = os.path.abspath(cfg_path)

        with open(file=cls.path, encoding="utf-8", mode="r") as f:
            parsed = json.load(f)

            # Convert list of kv pairs to dict
            for folder in parsed['folders']:
                cls.labels[folder['path']] = folder['summary']

    @classmethod
    def save(cls) -> None:
        # Convert dict to list of kv pairs
        buffer = {}

        buffer['folder'] = []
        for label in cls.labels:
            buffer['folder'].append({
                'path': label,
                'summary': cls.labels['label']
            })

        with open(file=cls.path, encoding='utf-8', mode="w") as f:
            json.dump(buffer, f)
    
    # # TODO: create config file if not exist
    # @classmethod
    # def create(cls, path:str = None) -> None:
    #     cls.path = os.path.abspath(path=path)
    #     with open(file=cls.path, mode="w+") as f:
            

    @classmethod
    def add_label(cls, label: str, summary: str) -> None:
        cls.labels[label] = summary


# if __name__ == '__main__':
#     Config.load()
#     Config.set_src_folder('test_files')

#     # Debug print
#     print(Config.labels)
#     print(Config.src_folder_path)
