import os
import sys

import uvicorn

# Stelle sicher, dass das app-Verzeichnis im Python-Pfad ist
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "app"))

# Optional: Konfiguration laden und anzeigen
config_path = os.path.join(os.path.dirname(__file__), "app", "config.json")
if os.path.exists(config_path):
    import json
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    print(f"Starte Server mit Modell: {config.get('MODEL_PATH')}")

if __name__ == "__main__":
    uvicorn.run("app.chat:app", host="0.0.0.0", port=8001, reload=True)
