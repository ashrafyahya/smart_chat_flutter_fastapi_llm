🛠️ Voraussetzungen (lokal)

Stelle sicher, dass folgende Software auf deinem System installiert ist:
Tool	Zweck	Check-Befehl
Node.js (v18+)	JS/TS-Laufzeit	node -v
npm (v9+)	Paketmanager	npm -v
Angular CLI	Projekt-Generator	ng version
VSCode	Code-Editor	✅ Visual Studio Code

❗ Falls du ng noch nicht installiert hast:
$npm install -g @angular/cli


🚀 Projekt initialisieren
1. Neues Angular-Projekt erstellen
$ ng new smart-chat-frontend --style=scss --routing=true


Erklärung der Optionen:

    --style=scss: Nutzt SCSS statt CSS (für professionelleres Styling)

    --routing=true: Aktiviert Angular-Routing direkt (z. B. für spätere Seiten wie /settings)

Während der Einrichtung wirst du gefragt:

    Would you like to add Angular routing? → Yes

    Which stylesheet format would you like to use? → SCSS

2. Projektverzeichnis betreten
$cd smart-chat-frontend


3. Angular Material hinzufügen
$ng add @angular/material

Setup-Auswahl:

    Theme: z. B. Indigo/Pink oder Custom

    Typography: Yes

    Animations: Yes


📦 Empfohlene Zusatzpakete

Installiere zusätzliche Tools für sauberen Code & gute Entwicklererfahrung:
$npm install --save-dev prettier eslint
$ng add @angular-eslint/schematics

▶️ Projekt starten

Starte den lokalen Entwicklungsserver:
$ng serve
Öffne deinen Browser:
http://localhost:4200
----------------------------------------------------------------------------
✅ 1. Node.js + npm installieren

    ⚠️ Wichtig: Angular benötigt Node.js ≥ 18 und npm ≥ 9.

🔹 Schritt A: Version prüfen
$node -v
$npm -v


🔹 Schritt B: Wenn Node.js nicht installiert ist (oder zu alt):

    Gehe auf: https://nodejs.org

    Lade die LTS-Version (18.x oder höher) herunter und installiere sie

    Nach der Installation erneut prüfen:
    $node -v
    $npm -v


✅ 2. Angular CLI installieren

    Die Angular CLI ist das Hauptwerkzeug für Angular-Projekte.

🔹 Installation:
$npm install -g @angular/cli


🔹 Version prüfen:
$ng version


🔄 Zusammenfassung der Befehle:
```bash
# Node.js & npm prüfen
node -v
npm -v

# Angular CLI installieren
npm install -g @angular/cli

# Angular CLI prüfen
ng version

```

Node.js: Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts.
-----------------------------------------------------------------
🧱 Schritt 1: Projektstruktur planen

src/app/
├── core/           → Dienste (Services), zentrale Konfiguration
├── shared/         → Wiederverwendbare Komponenten, Pipes, Interfaces
├── chat/           → Feature-Modul: Chat-Komponenten & Logik
├── app-routing.module.ts
└── app.module.ts
