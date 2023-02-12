import json
import os

template = {
    "folders": [],
}

class Config:
    path: str = None
    labels = {}
    src_folder_path = None
    


    @classmethod
    def load(cls, cfg_path) -> None:

        cls.path = os.path.abspath(cfg_path)

        with open(file=cls.path, encoding="utf-8", mode="r") as f:
            parsed = json.load(f)

            cls.src_folder_path = os.path.abspath(parsed['src_folder_path'])

            # Convert list of kv pairs to dict
            for folder in parsed['folders']:
                cls.labels[folder['path']] = folder['summary']

    @classmethod
    def save(cls) -> None:
        # Convert dict to list of kv pairs
        buffer = {}
        buffer['src_folder_path'] = os.path.abspath(
            cls.src_folder_path)  # redunant but might as well

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
    def set_src_folder(cls, path: str) -> None:
        cls.src_folder_path = os.path.abspath(path)

    @classmethod
    def add_label(cls, label: str, summary: str) -> None:
        cls.labels[label] = summary


# if __name__ == '__main__':
#     Config.load()
#     Config.set_src_folder('test_files')

#     # Debug print
#     print(Config.labels)
#     print(Config.src_folder_path)
