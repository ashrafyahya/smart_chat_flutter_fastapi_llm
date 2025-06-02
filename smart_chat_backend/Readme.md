# 🧠 LLM Chat Backend (FastAPI + GPT4All)

Ein leichtgewichtiges, vollständig **offline** laufendes Backend für ein Smart-Chat-System mit einem lokalen LLM (Large Language Model), wie z. B. **GPT4All** oder **LLaMA (gguf)**.  
Ideal für Flutter-Apps oder andere Clients, die lokal mit einem Chatmodell kommunizieren sollen.

---

## 🎯 Ziel

- Bereitstellung einer HTTP-API (`/chat`) zur Kommunikation mit einem lokalen KI-Modell.
- Offline-Nutzung ohne Internet.
- Schnelle Antworten durch quantisierte Modelle (gguf).
- Modularer Aufbau für spätere Integration mit anderen Modellen (transformers, llama.cpp, etc.).

---

## 📁 Projektstruktur

```plaintext
smart_chat_backend/
├── app/
│   ├── main.py          # FastAPI entrypoint
│   ├── model.py         # Modellanbindung GPT4All / LLaMA
│   └── schemas.py       # Datenmodelle (Pydantic)
├── requirements.txt     # Python-Abhängigkeiten
└── README.md            # Dieses Dokument


🚀 Installation
1. 📦 Voraussetzungen

    Python 3.9+

    Windows, macOS oder Linux

    mind. 8 GB RAM empfohlen (je nach Modell)



2. 🔧 Setup
# Projekt klonen oder neu anlegen
git clone <dieses-repo> smart_chat_backend
cd smart_chat_backend

# Virtuelle Umgebung erstellen
python -m venv .venv
.venv\Scripts\activate   # Windows

# Abhängigkeiten installieren
pip install -r requirements.txt


3. 🧠 Modell vorbereiten
GPT4All-Modell

    Lade ein Modell von https://gpt4all.io/models herunter.
    Beispiel: mistral-7b-openorca.Q4_0.gguf

    Platziere das Modell im GPT4All-Verzeichnis:
    C:\Users\<DeinBenutzer>\.gpt4all\models\
    oder passe den Pfad in app/model.py an:
    MODEL_PATH = "Pfad/zum/deinem/modell.gguf"


▶️ Starten des Servers
uvicorn app.main:app --reload


Läuft auf:
📍 http://127.0.0.1:8000

Swagger-Doku (Testoberfläche):
📄 http://127.0.0.1:8000/docs
---------------------------------------------------------------------
Server starten:
$python server.py


Anfrage an Server schicken:
curl -X POST "http://localhost:8000/generate" ^
     -H "Content-Type: application/json" ^
     -d "{\"prompt\": \"Was ist die Hauptstadt von Deutschland?\"}"


