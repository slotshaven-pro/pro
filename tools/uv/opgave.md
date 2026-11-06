# Opgave med uv

Nu skal bruge uv til at administrere nye projekter og dit eget projekt.


## Brug uv til dit projekt

Opret dit Python-projekt Telefonbog som et uv-projekt med "uv init"

```bash
cd telefonbog
uv init # vi behøver ikke navn i et eksisterende projekt.
```

Bemærk, vi behøver ikke navn eller `no-package` i et eksisterende projekt.

## Installer et modul

Importér fx Datetime til dit projekt.

```python
from datetime import datetime as dt
```

Print tidspunkt når programmet køres.
```python
now = dt.now()
# Formateret som tekst
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Klokken er:", formatted)

```

## Gem projektets afhængigheder

Kommandoen opretter en såkaldt `lock`-fil.

```bash
uv lock
```

## Læs projekt-filerne

uv har nu tilføjet

| Fil | Indhold |
|---|---|
| `pyproject.toml` | Projektets navn, Python-version og moduler |
| `uv.lock` | Præcise versioner af alle moduler |
| `.python-version` | Python-versionen projektet bruger |

Kig i alle filerne og tjek ud hvad de indeholder.

## Push det til GitHub
Læg nyeste version med Datetime på Github.

## Hent naboens projekt

Hent nu din nabos projekt og få det til at virke med uv.
