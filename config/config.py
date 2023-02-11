import json


class Config:
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.labels = {}
        self.src_folder_path = None

    def load(self):
        # TODO: create config file if not exist
        with open(file=self.path, encoding="utf-8", mode="r") as f:
            parsed = json.load(f)

            self.src_folder_path = parsed['src_folder_path']

            # Convert list of kv pairs to dict
            for folder in parsed['folders']:
                self.labels[folder['path']] = folder['summary']

    def save(self):
        # Convert dict to list of kv pairs
        buffer = {}
        buffer['src_folder_path'] = self.src_folder_path

        buffer['folder'] = []
        for label in self.labels:
            buffer['folder'].append({
                'path': label,
                'summary': self.labels['label']
            })

        with open(file=self.path, encoding='utf-8', mode="w") as f:
            json.dumps(buffer)

    def set_src_folder(self, path: str):
        self.src_folder_path = path

    def add_label(self, label: str, summary: str):
        self.labels[label] = summary


if __name__ == '__main__':
    config = Config('config.example.json')
    config.load()
    config.set_src_folder('test_files')

    # Debug print
    print(config.labels)
    print(config.src_folder_path)
