import os
import json

# Modellpfad aus JSON laden (wie gehabt)
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    _json_config = json.load(f)
MODEL_PATH = _json_config["MODEL_PATH"]

# Server-Konfiguration
APP_MODULE = "app.chat:app"
HOST = "0.0.0.0"
PORT = 8000
