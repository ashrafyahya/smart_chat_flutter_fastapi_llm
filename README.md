# 🧠 smart_chat – Lokales Chat-System mit Flutter + FastAPI

## 1. Projektübersicht

**Projekttitel:** Smart Chat  
**Ziel:** Erstellung eines komplett lokal laufenden Chat-Systems mit moderner UI, lokalem LLM-Backend und klarer Trennung zwischen Frontend (Flutter) und Backend (FastAPI).

**Technologien:**

- **Frontend:** Flutter (für Web & Desktop, optional mobil), UI mit Themes & Custom Widgets
- **Backend:** Python (FastAPI), lokales LLM (z. B. llama.cpp, GPT4All, transformers mit quantisierten Modellen)
- **Kommunikation:** REST API (optional WebSocket für Streaming)

---

## 📋 2. Anforderungen (funktional & nicht-funktional)

### 🔷 Frontend (Flutter)

**Funktionale Anforderungen:**

- Chatfenster mit Nachrichtenein- und -ausgabe
- Historie von Konversationen
- Ladeindikator, wenn das Modell antwortet
- Fehleranzeige bei Backend-Problemen
- Eingabefeld mit "Senden"-Button + Enter-Key Support
- Responsives Design (Web & mobilfähig)

**Erweiterungen (später möglich):**

- Rollenwechsel (User / System / Assistant)
- Konversationsverwaltung (löschen, speichern, umbenennen)
- Theme-Switch (hell/dunkel)
- Spracheinstellungen

### 🔶 Backend (Python)

**Funktionale Anforderungen:**

- REST-API für Chat-Endpunkt (`/api/chat`)
- Integration eines lokalen LLM:
  - Einfaches Modell für schnellen Start: z. B. ggml, llama.cpp, GPT4All, mistral quantisiert
- Optional: Session-Verwaltung (für Chatverläufe)
- Logging von Fehlern und Anfragen
- Einfache Konfigurationsdatei (`config.yaml` oder `.env`)
- CORS aktivieren für Flutter-Web-Kommunikation

**Erweiterungen:**

- WebSocket-Support (Streaming)
- Mehrere Modelle unterstützen
- API-Key-basierte Authentifizierung

---

## 🛠️ 3. Software & Tools (lokal installieren)

### 🔧 Frontend (Flutter)

| Tool           | Zweck                                |
|----------------|---------------------------------------|
| Flutter SDK    | Cross-Plattform UI-Toolkit            |
| Dart SDK       | Programmiersprache (wird mit Flutter geliefert) |
| VS Code        | Code-Editor mit Flutter Plugin        |
| Emulator       | Optional: Android Emulator oder iOS Simulator |

**Installationsbefehle (Flutter):**

```bash
# Flutter SDK prüfen (mind. Flutter 3.x)
flutter --version

# Neues Projekt anlegen
flutter create smart_chat_frontend
cd smart_chat_frontend

# Abhängigkeiten hinzufügen
flutter pub add provider go_router http flutter_hooks flutter_svg
```

**Empfohlene Entwicklungsstruktur:**

- Nutze `provider` oder `flutter_hooks` für State Management
- `go_router` für Routing
- Custom Widgets & ThemeData für UI

---

### 🐍 Backend (FastAPI)

| Tool             | Zweck                            |
|------------------|-----------------------------------|
| Python 3.10+     | Laufzeitumgebung                 |
| FastAPI          | API-Framework                    |
| uvicorn          | ASGI Server                      |
| dotenv           | Umgebungsvariablen               |
| LLM Wrapper      | z. B. llama-cpp-python, transformers |
| Virtualenv       | Isolierte Umgebung               |

**Installationsbefehle (Backend):**

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install fastapi uvicorn python-dotenv
# Optional je nach Modell
pip install llama-cpp-python
pip install transformers
```

---

## 📁 4. Projektstruktur (Vorschlag)

```txt
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
│   └── smart_chat_frontend/
│       ├── lib/
│       │   ├── main.dart
│       │   ├── app/
│       │   │   ├── app.dart
│       │   │   ├── app_router.dart
│       │   │   └── app_theme.dart
│       │   ├── features/
│       │   │   └── chat/
│       │   │       ├── data/
│       │   │       ├── domain/
│       │   │       └── presentation/
│       │   ├── shared/
│       │   │   └── widgets/
│       └── pubspec.yaml
└── README.md
```

---

## ▶️ 5. Entwicklung starten

### Frontend

```bash
cd frontend/smart_chat_frontend
flutter run -d chrome     # für Web
flutter run -d windows    # für Windows Desktop
```

### Backend

```bash
cd backend/app
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

> API erreichbar unter: `http://127.0.0.1:8000/api/chat`

---

## 🧪 6. Testen & Debugging

**Flutter:**

```bash
flutter analyze       # Linting
flutter test          # Unit-Tests (wenn vorhanden)
flutter format .      # Code-Formatierung
```

**Backend:**

```bash
pytest                # Falls Tests vorhanden
```

---

## 📚 7. Nützliche Links

- [Flutter Docs](https://docs.flutter.dev)
- [Dart Language](https://dart.dev)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Llama.cpp](https://github.com/ggerganov/llama.cpp)
- [Transformers (HF)](https://huggingface.co/docs/transformers/index)
