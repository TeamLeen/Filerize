import json

import eel
import wx

import config


@eel.expose
def get_config_file_content():
    # 
    with open("./config.json", "r") as config_file:
        config_json = json.loads(config_file.read())
    return config_json


@eel.expose
def add_new_folder(folder_path, folder_summary):
    with open("./config.json", "r") as config_file:
        config_json = json.loads(config_file.read())

    config_json["folders"].append({
        "path": folder_path,
        "summary": folder_summary
    })

    with open("./config.json", "w") as config_file:
        config_file.write(json.dumps(config_json))

    return True


@eel.expose
def choose_folder():
    app = wx.App(None)
    folder = wx.DirSelector(message="select")
    return folder


@eel.expose
def delete_folder(folder_path):
    with open("./config.json", "r") as config_file:
        config_json = json.loads(config_file.read())

    folders = [folder for folder in config_json["folders"]
               if folder["path"] != folder_path]
    config_json["folders"] = folders

    with open("./config.json", "w") as config_file:
        config_file.write(json.dumps(config_json))

    return True


@eel.expose
def get_source_folder_path():
    with open("./config.json", "r") as config_file:
        config_json = json.loads(config_file.read())
    return config_json["src_folder_path"]


@eel.expose
def set_source_folder_path(new_path):
    with open("./config.json", "r") as config_file:
        config_json = json.loads(config_file.read())

    config_json["src_folder_path"] = new_path

    with open("./config.json", "w") as config_file:
        config_file.write(json.dumps(config_json))


eel.init('web')
eel.start('index.html', size=(1078, 800))
