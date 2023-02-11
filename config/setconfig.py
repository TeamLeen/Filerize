import json

def LoadJson(file):
    with open(file=file, encoding="utf-8", mode="r") as f:
        return json.load(f)

def InitConfig():
    data = LoadJson(".\\config.example.json")
    print(data)
