# Biblioteker og moduler i Python

## Hvad er et modul?

Et modul er den mindste kodeenhed i Python. Det er én enkelt `.py`-fil, som indeholder funktioner, klasser, variabler osv.

Moduler skal _importeres_ med `import [filnavn]` (uden `.py`), før de kan bruges.

```python
import my_library
from random import randint
```

## Hvad er et bibliotek?

Et bibliotek (eng. _package_) er (som regel) en samling af moduler.

```python
import requests
from PIL import Image
```

At lave sit eget bibliotek er lidt mere indviklet end at lave et simpelt modul.

## Typer af moduler og biblioteker

Der er grundlæggende tre slags:

1. **Python Standard Library (PSL)** – følger med Python (f.eks. `random`, `math`, `datetime`)
2. **Eksternt bibliotek** – tredjeparts-pakker, der installeres med `pip` (f.eks. `requests`, `Pillow`)
3. **Eget modul eller bibliotek** – `my_library.py`

Det er vigtigt at kende forskellen på de forskellige typer biblioteker, fordi nogle biblioteker skal _installeres_ med `pip install`, før de kan importeres.

### Python Standard Library

Bibliotekerne i PSL følger med Python-installationen. Det betyder:

- Moduler som `random`, `math`, `os`, `datetime` osv. er klar til brug.
- Du behøver ikke installere dem – du kan bare skrive `import random`.

Det samme gælder dine egne moduler/pakker.

### Eksterne biblioteker

Eksterne biblioteker "følger ikke med" Python. De er skabt af andre udviklere (tredjepart) og ligger som pakker på _Python Package Index_ (PyPI).

For at kunne bruge dem, skal du først installere dem med **`pip`**.

Eksempler:

```bash
pip install requests
pip install Pillow
```

Efter installation kan de importeres ligesom andre moduler:

```python
import requests
from PIL import Image
```

Bemærk: Navnet, du installerer med, er ikke altid det samme som navnet, du importerer. Pakken `Pillow` importeres f.eks. som `PIL`.

### Eget modul

Så simpelt som at oprette en Python-fil, f.eks. `my_module.py`, i samme mappe som dit program.

### Opsummering

Kort sagt:

- **PSL-moduler**: ingen installation, følger med Python
- **Eksterne biblioteker**: kræver `pip install`, fordi de ikke følger med Python
- **Egne filer**: ligger lokalt og kræver derfor ingen `pip`

## Hvordan finder Python dine pakker?

Python leder efter moduler i listen `sys.path` – i denne rækkefølge:

```text
sys.path
├── Projektmappe
├── Virtuelt miljø (venv)
├── Standardbibliotek (PSL)
└── Installerede pakker (pip)
```

## Syntaks

Der er mange måder at importere pakker og moduler på. To almindelige måder ses her:

```python
import [module] # file, package
from [module] import [name] # class, function, variable
```

Den afgørende forskel er, hvordan _namespaces_ (da. _navnerum_) håndteres.
Bemærk forskellen i dette eksempel.

```python
import random
result = random.randint(0, 5)

from random import randint
result = randint(0, 5)
```

### Alias

Med `as` kan du give et modul eller en funktion et andet (typisk kortere) navn:

```python
import [module] as [alias]
from [module] import [name] as [alias]
```

Nogle biblioteker har faste aliasser, som næsten alle bruger:

```python
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

today = dt.date.today()
```

## Eksempler

Her følger nogle eksempler. Kopiér dem til en notebook eller en `.py`-fil, og test, hvordan de fungerer.

```python
# Import file (own library)
import my_module
result = my_module.add_numbers(12, 17)

# Import file with module alias ("mm")
import my_module as mm
result = mm.add_numbers(12, 17)

# Import file with function alias ("plus")
from my_module import add_numbers as plus
result = plus(12, 17)

# Import everything from module
# Note: no namespace, risk of namespace clobbering
from my_module import *
result = add_numbers(12, 17)

# Import module random from PSL
# Note: with namespace
import random
result = random.randint(0, 5)

# Import function "randint()" from module "random" from PSL
# Note: no namespace, risk of namespace clobbering
from random import randint
result = randint(0, 5)
```
