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


## 🚀 Projekt
### 🧱 Projektstruktur

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
├── shared/   


### 🔧 Setup

- Projekt klonen: 
```sh
git clone https://github.com/ashrafyahya/smart_chat.git
cd smart_chat_frontend
```

- Zum Installieren der Abhängigkeiten führe im Projektverzeichnis aus:

```bash
flutter pub get
```


- Projekt starten
```flutter build web```
```flutter run```


### Wie kann ein Flutter Projekt angelegt werden?

-Nutze den folgenden Befehl:
```bash
flutter create Projek-Name 
```

- Projektverzeichnis betreten
$cd Projekt-Name


### Tooling & Linting
Formatieren
```flutter format .```

Analysieren
```flutter analyze```

Dart Language
https://dart.dev/


Eigene Notizen
- start ms-settings:developers
- flutter pub outdated
- flutter pub upgrade
- flutter pub upgrade --major-versions