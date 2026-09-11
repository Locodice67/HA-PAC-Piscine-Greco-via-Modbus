# HA — PAC Piscine Geco via Modbus

Intégration personnalisée Home Assistant pour la **PAC (pompe à chaleur) de piscine
Geco** (modèle **GEPAC08**, contrôleurs proches des cartes MWH216 / MWH298)
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

## Matériel de référence

Valeurs relevées sur la plaque signalétique de l'unité de développement.

**GECO — Swimming Pool Heat Pump — modèle `GEPAC08`** (compresseur **INVERTER**)

| Donnée | Valeur | Conditions |
|---|---|---|
| Puissance chauffage | 8,4 kW | air 26 °C / eau 26 °C / 80 % HR |
| COP | 14,1 ~ 7,0 | idem |
| COP à 50 % | 10,3 | idem |
| Puissance chauffage | 6,1 kW | air 15 °C / eau 26 °C / 70 % HR |
| COP | 7,0 ~ 4,8 | idem |
| COP à 50 % | 6,3 | idem |
| Puissance froid | 4,0 kW | air 35 °C / eau 28 °C / 80 % HR |
| Alimentation | 230 V / 1 Ph / 50 Hz | — |
| Pression sonore à 1 m | 38,8 ~ 48,2 dB(A) | — |
| Pression sonore à 50 % | 41,4 dB(A) | — |
| Puissance absorbée | 0,17 ~ 1,2 kW | air 15 °C |
| Courant absorbé | 0,74 ~ 5,2 A | air 15 °C |
| Courant max | 8,5 A | — |
| Débit d'eau conseillé | 2 ~ 4 m³/h | — |
| Fluide frigorigène | R32 — 650 g | GWP 675 · éq. CO₂ 0,439 t |
| Indice de protection | IPX4 | — |
| Poids | 45 kg | — |

La fiche Modbus officielle des cartes **MWH216 / MWH298** s'applique à cette unité.

## Avertissement

Les adresses de registres proviennent de la fiche Modbus officielle des cartes
MWH216 / MWH298 et d'un projet communautaire de rétro-ingénierie. Les cartes
Geco / AES / Madimack se ressemblent beaucoup, mais le modèle exact peut différer.
**Vérifie les valeurs (températures eau/air en particulier) contre les mesures
réelles avant toute mise en production.**
