# smart_chat🧩 1. Projektübersicht

Projekttitel: Smart Chat
Ziel: Erstellung eines komplett lokal laufenden Chat-Systems mit moderner UI, lokalem LLM-Backend und klarer Trennung zwischen Frontend und Backend.
Technologien:

    Frontend: Angular + UI-Framework (z. B. Angular Material oder Tailwind + Custom Components)

    Backend: Python (FastAPI), lokales LLM (z. B. llama.cpp, GPT4All, transformers mit quantisierten Modellen)

    Kommunikation: REST API (optional WebSocket für Streaming)

📋 2. Anforderungen (funktional & nicht-funktional)
🔷 Frontend (Angular)
Funktionale Anforderungen:

    Chatfenster mit Nachrichtenein- und -ausgabe

    Historie von Konversationen

    Ladeindikator, wenn das Modell antwortet

    Fehleranzeige bei Backend-Problemen

    Eingabefeld mit "Senden"-Button + Enter-Key Support

    Responsives Design (mobilfähig)

Erweiterungen (später möglich):

    Rollenwechsel (User / System / Assistant)

    Konversationsverwaltung (löschen, speichern, umbenennen)

    Theme-Switch (hell/dunkel)

    Spracheinstellungen

🔶 Backend (Python)
Funktionale Anforderungen:

    REST-API für Chat-Endpunkt (/api/chat)

    Integration eines lokalen LLM:

        Einfaches Modell für schnellen Start: z. B. ggml, llama.cpp, GPT4All, mistral quantisiert

    Optional: Session-Verwaltung (für Chatverläufe)

    Logging von Fehlern und Anfragen

    Einfache Konfigurationsdatei (config.yaml oder .env)

    CORS aktivieren für Angular-Kommunikation

Erweiterungen:

    WebSocket-Support (Streaming)

    Mehrere Modelle unterstützen

    API-Key-basierte Authentifizierung

🛠️ 3. Software & Tools (lokal installieren)
🔧 Frontend
Tool	Zweck
Node.js	Runtime für Angular
Angular CLI	Projektverwaltung, Build, Serve
UI-Framework	z. B. Angular Material, Tailwind CSS
VSCode Extensions	Angular Essentials, ESLint, Prettier, etc.
Installationsbefehle:

```bash 
npm install -g @angular/cli 
ng new smart-chat-frontend
cd smart-chat-frontend
ng add @angular/material
```

🐍 Backend
Tool	Zweck
Python 3.10+	Laufzeitumgebung
FastAPI	API-Framework
uvicorn	ASGI Server
httpx / requests	Optionale HTTP-Clients
LLM-Wrapper	z. B. llama-cpp-python, transformers
Virtualenv	für isolierte Umgebungen
Installationsbefehle:
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install fastapi uvicorn python-dotenv
# Optional je nach Modell
pip install llama-cpp-python
pip install transformers
```

📁 4. Projektstruktur (Vorschlag)
📦 Gesamtstruktur
smart-chat/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── chat.py
│   │   ├── model/
│   │   │   └── llama_wrapper.py
│   │   └── config.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   └── smart-chat-frontend/
│       ├── src/
│       │   ├── app/
│       │   │   ├── chat/
│       │   │   └── shared/
│       └── angular.json
└── README.md


