# 🧠 Smart Chat Frontend (Flutter Version)

## 🛠️ Voraussetzungen (lokal)

Stelle sicher, dass folgende Software auf deinem System installiert ist:

| Tool             | Zweck                        | Check-Befehl             |
|------------------|-------------------------------|--------------------------|
| Flutter SDK      | UI-Framework für Mobile/Web   | `flutter --version`      |
| Dart SDK         | Programmiersprache            | Wird mit Flutter geliefert |
| VS Code          | Code-Editor                   | ✅ Visual Studio Code     |
| Android Studio   | Emulator + SDK Manager        | ✅ empfohlen für Android  |

❗ Wenn du Flutter noch nicht installiert hast:  
👉 [Flutter Installation Guide](https://docs.flutter.dev/get-started/install)

## 🚀 Projekt initialisieren

### 1. Neues Flutter-Projekt erstellen

```bash
flutter create smart_chat_frontend 
```

### 2. Projektverzeichnis betreten
$cd smart-chat-frontend



## 📦 Empfohlene Zusatzpakete

Installiere zusätzliche Pakete für bessere Struktur und Features:

```bash
flutter pub add provider
flutter pub add flutter_hooks
flutter pub add go_router
flutter pub add flutter_svg
flutter pub add http
```
➕ Dev-Dependencies (für Codequalität)
```bash
flutter pub add --dev very_good_analysis
flutter pub add --dev flutter_lints 
```



## ▶️ Projekt starten
Starte deine App auf einem Emulator oder echten Gerät:
```flutter build web```
```flutter run```
----------------------------------------------------------------------------
-----------------------------------------------------------------
🧱 Schritt 1: Projektstruktur planen

lib/
├── main.dart                → Einstiegspunkt der App
├── app/                    → Routing, Theme, App-Shell
│   ├── app.dart
│   ├── app_router.dart
│   └── app_theme.dart
├── features/
│   └── chat/               → Chat-spezifische Logik & UI
│       ├── data/           → Modelle, APIs, DTOs
│       ├── domain/         → Services, Business Logic
│       └── presentation/   → UI-Komponenten (Widgets, Screens)
├── core/                   → Globale Dienste, Logging, Exceptions
├── shared/                 → Wiederverwendbare Widgets, Utils


✅ Tooling & Linting
Formatieren
```flutter format .```


Analysieren
```flutter analyze```

📱 Build für Web / Android / iOS
Web
```flutter build web```

Dart Language
https://dart.dev/


Eigene Notizen
- start ms-settings:developers
- flutter pub outdated
- flutter pub upgrade
- flutter pub upgrade --major-versions
- 