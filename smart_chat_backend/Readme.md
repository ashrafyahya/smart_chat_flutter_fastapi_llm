# 🧠 LLM Chat Backend (FastAPI + llama.cpp)

Ein leichtgewichtiges, vollständig **offline** laufendes Backend für ein Smart-Chat-System mit einem lokalen LLM (Large Language Model), z. B. **LLaMA (gguf)** über [llama.cpp](https://github.com/ggerganov/llama.cpp).  
Ideal für Flutter-Apps oder andere Clients, die lokal mit einem Chatmodell kommunizieren sollen.

---

## 🎯 Ziel

- Bereitstellung einer HTTP-API (`/generate`) zur Kommunikation mit einem lokalen KI-Modell.
- Offline-Nutzung ohne Internet.
- Schnelle Antworten durch quantisierte Modelle (gguf).
- Modularer Aufbau für spätere Integration mit anderen Modellen (transformers, llama.cpp, etc.).

---

## 📁 Projektstruktur

```plaintext
smart_chat_backend/
├── app/
│   ├── chat.py          # FastAPI entrypoint
│   ├── model.py         # Modellanbindung llama.cpp
├── config.py            # Projektweite Konfiguration (Modellpfad, Host, Port)
├── requirements.txt     # Python-Abhängigkeiten
├── server.py            # Startet den Server
└── README.md            # Dieses Dokument
```

---

## 🚀 Installation

1. 📦 Voraussetzungen

    - Python 3.9+
    - Windows, macOS oder Linux
    - mind. 8 GB RAM empfohlen (je nach Modell)

2. 🔧 Setup

    ```sh
    # Projekt klonen oder neu anlegen
    git clone <dieses-repo> smart_chat_backend
    cd smart_chat_backend

    # Virtuelle Umgebung erstellen
    python -m venv .venv
    .venv\Scripts\activate   # Windows

    # Abhängigkeiten installieren
    pip install -r requirements.txt
    ```

3. 🧠 Modell vorbereiten

    - Lade ein GGUF-Modell von z.B. [TheBloke](https://huggingface.co/TheBloke) oder anderen Quellen herunter.
    - Beispiel: mistral-7b-openorca.Q4_0.gguf
    - Passe den Pfad in `config.py` an:
      ```python
      MODEL_PATH = "Pfad/zum/deinem/modell.gguf"
      ```

---

## ▶️ Starten des Servers

```sh
python server.py
```
Mit --reload: Server startet bei jeder Änderung automatisch neu (nur für Entwicklung empfohlen)

Läuft auf:  
📍 http://127.0.0.1:8000

Swagger-Doku (Testoberfläche):  
📄 http://127.0.0.1:8000/docs

---

## Anfrage an Server schicken

```sh
curl -X POST "http://localhost:8000/generate" 
    -H "Content-Type: application/json" 
    -d "{\"prompt\": \"Was ist die Hauptstadt von Deutschland?\"}"
```


