# 🧠 Smart Chat Frontend (Flutter Version)

## 🛠️ Voraussetzungen (lokal)

Stelle sicher, dass folgende Software auf deinem System installiert ist:

| Tool             | Zweck                        | Check-Befehl             |
|------------------|-------------------------------|--------------------------|
| Flutter SDK      | UI-Framework für Mobile/Web   | `flutter --version`      |
| Dart SDK         | Programmiersprache            | Wird mit Flutter geliefert |
| VS Code          | Code-Editor                   | ✅ Visual Studio Code     |

❗ Wenn du Flutter noch nicht installiert hast:  
👉 [Flutter Installation Guide](https://docs.flutter.dev/get-started/install)

## 🚀 Projekt initialisieren

### 1. Neues Flutter-Projekt erstellen

```bash
flutter create smart_chat_frontend 
```

### 2. Projektverzeichnis betreten
$cd smart-chat-frontend



## 📦 Dependencies

Die Abhängigkeiten werden im `pubspec.yaml` verwaltet. Die wichtigsten Pakete in diesem Projekt sind:

➕ Dev-Dependencies (für Codequalität)
```bash
flutter pub add --dev very_good_analysis
flutter pub add --dev flutter_lints 
```

**Dependencies:**
- flutter (SDK)
- provider: ^6.1.0
- flutter_hooks: ^0.21.2
- http: ^1.1.0
- share_plus: ^11.0.0

**Dev Dependencies:**
- flutter_test (SDK)
- flutter_lints: ^6.0.0

Zum Installieren der Abhängigkeiten führe im Projektverzeichnis aus:

```bash
flutter pub get
```



## ▶️ Projekt starten
Starte deine App auf einem Emulator oder echten Gerät:
```flutter build web```
```flutter run```
----------------------------------------------------------------------------
🧱 Projektstruktur planen

lib/
├── main.dart                   → Einstiegspunkt der App
├── features/chat               → Chat-spezifische Logik & UI
│   ├── data/                   → Modelle, APIs, DTOs
│       ├── chat_api.dart
│   ├── domain/                 → Services, Business Logic
│       ├── chat_message.dart
│   ├── presentaion/            → UI-Komponenten (Widgets, Screens)
│       ├── widgets/
│           ├── chat_bubble.dart
│       ├── chat_screen.dart
│   └── main.dart
├── core/                       → Globale Dienste, Logging, Exceptions
├── shared/                     → Wiederverwendbare Widgets, Utils


✅ Tooling & Linting
Formatieren
```flutter format .```


Analysieren
```flutter analyze```

📱 Build für Web / Android / iOS
- Web
```flutter build web```

Dart Language
https://dart.dev/


Eigene Notizen
- start ms-settings:developers
- flutter pub outdated
- flutter pub upgrade
- flutter pub upgrade --major-versions
- 