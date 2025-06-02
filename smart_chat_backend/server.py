import os
import sys

import uvicorn
from app.config import APP_MODULE, HOST, MODEL_PATH, PORT

# Stelle sicher, dass das app-Verzeichnis im Python-Pfad ist
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "app"))

# Optional: Modellpfad ausgeben
print(f"Starte Server mit Modell: {MODEL_PATH}")

if __name__ == "__main__":
    uvicorn.run(APP_MODULE, host=HOST, port=PORT, reload=True)
