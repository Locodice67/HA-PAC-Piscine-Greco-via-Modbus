# HA — PAC Piscine Geco via Modbus

Intégration personnalisée Home Assistant pour la **PAC (pompe à chaleur) de piscine
Geco** (modèle IPHCR45 et contrôleurs proches des séries Geco / AES / Madimack)
exposée en **Modbus TCP** via une passerelle RS485 → Ethernet.

## Entités créées

| Plateforme | Entité | Registre |
|---|---|---|
| `climate` | Thermostat (consigne, mode, ventilation) | input 3 / holding 3 / holding 0 / holding 1 |
| `switch` | Marche/Arrêt | coil 0 |
| `sensor` | Température eau | input 4 |
| `sensor` | Température air | input 5 |
| `sensor` | Intensité compresseur | input 11 |
| `sensor` | Tension PFC | input 2 |
| `sensor` | Compresseur | input 0 |
| `binary_sensor` | Status | coil 0 |
| `binary_sensor` | Défaut général | discrete input 16 |
| `binary_sensor` | Défaut E3 | discrete input 51 |
| `binary_sensor` | État communication Modbus | — (diagnostic) |
| `number` | Consigne température | holding 3 |
| `select` | Mode (Auto/Chaud/Froid) | holding 0 |
| `select` | Mode de travail (Smart/Silence/Super Silence) | holding 1 |

> `number` et les deux `select` écrivent **les mêmes registres** que le `climate`.
> C'est sans danger (toutes les entités relisent la valeur au même cycle de poll),
> mais il s'agit de vues alternatives : le `climate` suffit pour piloter la PAC.

## Installation

### HACS (dépôt personnalisé)

1. HACS → Intégrations → ⋯ → *Dépôts personnalisés*.
2. Ajouter `Locodice67/HA-PAC-Piscine-Geco-via-Modbus` en catégorie *Intégration*.
3. Installer, puis redémarrer Home Assistant.

### Manuelle

Copier le dossier `custom_components/pac_piscine_geco/` dans `/config/custom_components/`,
puis redémarrer Home Assistant.

## Configuration

Paramètres → Appareils et services → Ajouter une intégration → **PAC Piscine Geco**.

| Champ | Valeur usuelle |
|---|---|
| Adresse IP | IP de la passerelle RS485 → Ethernet branchée sur le port Modbus de la PAC |
| Port TCP | `4196` / `4197` selon la passerelle (Waveshare par défaut) |
| Adresse Modbus (esclave) | `1` |
| Intervalle de rafraîchissement | `30` s |

L'intervalle est modifiable ensuite via le bouton *Configurer* de l'intégration.

## Avertissement

Les adresses de registres proviennent d'un projet communautaire de rétro-ingénierie
sur une PAC Geco IPHCR45. Les cartes Geco / AES / Madimack se ressemblent beaucoup,
mais le modèle exact peut différer. **Vérifie les valeurs (températures eau/air en
particulier) contre les mesures réelles avant toute mise en production.**
