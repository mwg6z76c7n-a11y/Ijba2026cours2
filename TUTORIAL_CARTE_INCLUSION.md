# Tutoriel : Créer une carte interactive avec Leaflet et GitHub Pages

Ce guide vous explique comment transformer un fichier de données (CSV) en une carte interactive hébergée gratuitement sur le web.

## 1. Préparer vos données (Le fichier CSV)
Votre fichier doit être au format `.csv` et contenir au minimum trois colonnes avec ces noms exacts :
*   `nom` : Le nom du lieu.
*   `latitude` : La coordonnée nord (ex: 44.837).
*   `longitude` : La coordonnée est/ouest (ex: -0.579).

**Conseil :** Nommez votre fichier simplement, par exemple `lieux.csv`, sans espaces ni accents pour éviter les erreurs de lien.

---

## 2. Structure du fichier `index.html`
C'est le fichier qui contient votre carte. Voici les trois composants essentiels à inclure :

### A. Les bibliothèques (dans le `<head>`)
Vous devez appeler Leaflet (pour la carte) et PapaParse (pour lire le CSV).
```html
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>
```

### B. Le conteneur de la carte (dans le `<body>`)
```html
<div id="map" style="height: 100vh; width: 100vw;"></div>
```

### C. Le script JavaScript
C'est ici que la magie opère :
1. **Initialiser la carte** : `const map = L.map('map').setView([lat, lon], zoom);`
2. **Charger le fond de carte** : Utilisez OpenStreetMap.
3. **Lire le CSV** : Utilisez `Papa.parse()`.
4. **Créer les marqueurs** : Bouclez sur chaque ligne du CSV pour ajouter un point GPS.

---

## 3. Personnaliser les marqueurs (Les cœurs roses)
Pour remplacer les points bleus par des cœurs, on utilise un format SVG pour que ce soit joli et robuste :

```javascript
const heartIcon = L.divIcon({
    className: 'custom-icon',
    html: '<svg width="30" height="30" viewBox="0 0 24 24" fill="#ff69b4" xmlns="http://www.w3.org/2000/svg"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>',
    iconSize: [30, 30],
    iconAnchor: [15, 15]
});
```

---

## 4. Publier sur GitHub Pages
Une fois que vos fichiers `index.html` et `lieux.csv` sont sur votre dépôt GitHub :

1. Allez dans les **Settings** de votre dépôt.
2. Cliquez sur **Pages** (colonne de gauche).
3. Sous "Build and deployment", choisissez la branche **main** et le dossier **/(root)**.
4. Cliquez sur **Save**.
5. Votre site sera disponible à l'adresse : `https://votre-pseudo.github.io/nom-du-depot/`

---

## 5. Mises à jour futures
L'avantage de cette méthode (PapaParse) est la simplicité :
*   Si vous voulez ajouter un lieu, modifiez simplement votre fichier **CSV**.
*   Dès que vous "pushez" le CSV sur GitHub, la carte se mettra à jour automatiquement pour tous les visiteurs.
