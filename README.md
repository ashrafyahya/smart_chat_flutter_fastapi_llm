# 🧠 smart_chat – Lokales Chat-System mit Flutter + FastAPI

## 1. Projektübersicht

**Projekttitel:** Smart Chat  
**Ziel:** Erstellung eines komplett lokal laufenden Chat-Systems mit moderner UI, lokalem LLM-Backend und klarer Trennung zwischen Frontend (Flutter) und Backend (FastAPI).

**Technologien:**

- **Frontend:** Flutter (für Web & Desktop u. ggf. mobil), UI mit Themes & Custom Widgets
- **Backend:** Python (FastAPI), lokales LLM (z. B. llama.cpp, GPT4All, transformers mit quantisierten Modellen)
- **Kommunikation:** REST API (optional WebSocket für Streaming)

---

## 📋 2. Anforderungen (funktional & nicht-funktional)

### 🔷 Frontend (Flutter)

**Funktionale Anforderungen:**

- Chatfenster mit Nachrichtenein- und -ausgabe
- Ladeindikator, wenn das Modell antwortet
- Fehleranzeige bei Backend-Problemen
- Eingabefeld mit "Senden"-Button + Enter-Key Support
- Responsives Design (Web & mobilfähig)

**Erweiterungen (Backlog):**
- Historie von Konversationen
- Rollenwechsel (User / System / Assistant)
- Konversationsverwaltung (löschen, speichern, umbenennen)
- Theme-Switch (hell/dunkel)
- Spracheinstellungen

### 🔶 Backend (Python)

**Funktionale Anforderungen:**

- REST-API für Chat-Endpunkt (`/api/chat`)
- Integration eines lokalen LLM:
  - Einfaches Modell für schnellen Start: z. B. ggml, llama.cpp, GPT4All, mistral quantisiert
- WebSocket-Support (Streaming)
- Logging von Fehlern und Anfragen
- Einfache Konfigurationsdatei (`config.py`)
- CORS aktivieren für Flutter-Web-Kommunikation

**Erweiterungen:**
- Session-Verwaltung (für Chatverläufe)
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


### 🐍 Backend (FastAPI)

| Tool             | Zweck                            |
|------------------|-----------------------------------|
| Python 3.10+     | Laufzeitumgebung                 |
| FastAPI          | API-Framework                    |
| uvicorn          | ASGI Server                      |
| dotenv           | Umgebungsvariablen               |
| LLM Wrapper      | z. B. llama-cpp-python           |
| Virtualenv       | Isolierte Umgebung               |

## 📁 4. Projektstruktur (Vorschlag)

```txt
smart-chat/
├── backend/
├── frontend/
└── README.md
```
## 🧪 Testen & Debugging

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
