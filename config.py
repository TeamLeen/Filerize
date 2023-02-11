import json


class Config:
    path: str = r"D:\dev\hacknotts\23\Filerize\config.example.json"
    labels = {}
    src_folder_path = None

    @classmethod
    def load(cls) -> None:
        # TODO: create config file if not exist
        with open(file=cls.path, encoding="utf-8", mode="r") as f:
            parsed = json.load(f)

            cls.src_folder_path = parsed['src_folder_path']

            # Convert list of kv pairs to dict
            for folder in parsed['folders']:
                cls.labels[folder['path']] = folder['summary']

    @classmethod
    def save(cls) -> None:
        # Convert dict to list of kv pairs
        buffer = {}
        buffer['src_folder_path'] = cls.src_folder_path

        buffer['folder'] = []
        for label in cls.labels:
            buffer['folder'].append({
                'path': label,
                'summary': cls.labels['label']
            })

        with open(file=cls.path, encoding='utf-8', mode="w") as f:
            json.dump(buffer, f)

    @classmethod
    def set_src_folder(cls, path: str) -> None:
        cls.src_folder_path = path

    @classmethod
    def add_label(cls, label: str, summary: str) -> None:
        cls.labels[label] = summary

    @classmethod
    def set_path(cls, path: str):
        cls.path = path


if __name__ == '__main__':
    Config.load()
    Config.set_src_folder('test_files')

    # Debug print
    print(Config.labels)
    print(Config.src_folder_path)
