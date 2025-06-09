# 🧠 LLM Chat Backend (FastAPI + llama.cpp)

Ein leichtgewichtiges, vollständig **offline** laufendes Backend für ein Smart-Chat-System mit einem lokalen LLM (Large Language Model), z. B. **LLaMA (gguf)** über [llama.cpp](https://github.com/ggerganov/llama.cpp).  
Ideal für Apps oder andere Clients, die lokal mit einem Chatmodell kommunizieren sollen.

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
│   ├── memory.py        # Modell-Gedächtnis  
│   ├── model.py         # Modellanbindung llama.cpp
│   ├── prompt.py        # Prmpt für Modell
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
    git clone https://github.com/ashrafyahya/smart_chat.git
    cd smart_chat_backend

    # Virtuelle Umgebung erstellen bzw. starten
    python -m venv .venv     # Erstellen
    .venv\Scripts\activate   # Starten auf Windows

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

---

## Anfrage an Server schicken

```sh
curl -X POST "http://localhost:8000/generate" 
    -H "Content-Type: application/json" 
    -d "{\"prompt\": \"Was ist der Wert von PI?\"}"
```


