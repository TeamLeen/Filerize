import eel
import json

@eel.expose
def get_config_file_content():
    with open("./config.json", "r") as config_file:
        config_json = json.loads(config_file.read())
    return config_json

eel.init('web')
eel.start('index.html', size=(1078, 800))
