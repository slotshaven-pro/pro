# Kollektioner i Python – lister, dictionaries, tupler og sæt

Indtil nu har de fleste af vores variabler indeholdt **én** værdi: et tal, en tekst eller en sandhedsværdi.

```python
navn = "Ida"
alder = 17
```

Men programmer arbejder næsten altid med **mange** værdier på én gang: alle elever i en klasse, alle varer i en indkøbskurv, alle målinger fra en sensor. Til det bruger vi **kollektioner** (eng. _collections_) – datatyper, der kan holde på flere værdier samtidig.

Python har fire indbyggede kollektioner:

| Type | Dansk navn | Eksempel |
|---|---|---|
| `list` | liste | `["Ida", "Jon", "Kai"]` |
| `dict` | dictionary / opslagsliste / ordbog | `{"Ida": 12, "Jon": 7}` |
| `tuple` | tupel | `(55.68, 12.57)` |
| `set` | sæt / mængde | `{"rød", "grøn", "blå"}` |

I daglig tale kalder vi dem ofte bare "lister", men de har forskellige **egenskaber**, og derfor er de gode til forskellige ting.

---

## De fire egenskaber

For at forstå forskellen på de fire typer skal man kunne svare på fire spørgsmål.

### 1. Er den ordnet?

En kollektion er **ordnet**, hvis elementerne har en fast rækkefølge. Det element, der blev sat ind først, ligger først.

```python
dage = ["man", "tirs", "ons"]
print(dage)     # ['man', 'tirs', 'ons'] – altid i samme rækkefølge
```

Et **sæt** er _ikke_ ordnet. Python bestemmer selv rækkefølgen, og den kan se tilfældig ud:

```python
farver = {"rød", "grøn", "blå"}
print(farver)   # fx {'blå', 'rød', 'grøn'}
```

> **Bemærk:** Dictionaries husker den rækkefølge, nøglerne blev sat ind i (fra Python 3.7). Men man slår op med en **nøgle** – ikke med en position.

### 2. Kan den ændres (mutable)?

En kollektion er **mutable** (foranderlig), hvis man kan ændre, tilføje og fjerne elementer, efter den er oprettet.

```python
kurv = ["mælk", "brød"]
kurv.append("ost")      # OK – lister kan ændres
```

En **tupel** er **immutable** (uforanderlig). Når den først er lavet, kan den ikke ændres:

```python
punkt = (3, 4)
punkt[0] = 10           # TypeError: 'tuple' object does not support item assignment
```

### 3. Tillader den dubletter?

Kan den samme værdi optræde flere gange?

```python
karakterer = [7, 10, 7, 12]       # liste: 7 står to gange – helt fint
unikke = {7, 10, 7, 12}           # sæt: bliver til {10, 12, 7}
```

I et **dictionary** skal **nøglerne** være unikke. Værdierne må gerne være ens.

```python
alder = {"Ida": 17, "Jon": 17}    # to forskellige nøgler med samme værdi – OK
```

### 4. Hvordan får man fat i et element?

| Adgang | Typer | Eksempel |
|---|---|---|
| Via **indeks** (position, starter ved 0) | liste, tupel | `dage[0]` |
| Via **nøgle** | dictionary | `alder["Ida"]` |
| Ingen direkte adgang – kun "er den med?" | sæt | `"rød" in farver` |

---

## Overblik

| | `list` | `dict` | `tuple` | `set` |
|---|---|---|---|---|
| **Parenteser** | `[ ]` | `{ nøgle: værdi }` | `( )` | `{ }` |
| **Ordnet** | ja | ja (indsættelsesrækkefølge) | ja | nej |
| **Kan ændres** | ja | ja | **nej** | ja |
| **Dubletter** | ja | nøgler: nej / værdier: ja | ja | **nej** |
| **Adgang** | indeks `x[0]` | nøgle `x["navn"]` | indeks `x[0]` | kun `in` |
| **Tom** | `[]` | `{}` | `()` | `set()` |

> **Pas på med de krøllede parenteser!**
> `{}` er et **tomt dictionary** – ikke et tomt sæt. Et tomt sæt laves med `set()`.
> `{"a": 1}` er et dictionary (der er kolon). `{"a", "b"}` er et sæt (der er intet kolon).

> **Pas på med tupler med ét element!**
> `(5)` er bare tallet 5 i en parentes. En tupel med ét element skrives `(5,)` – med komma.

---

## De fire typer kort fortalt

### Liste – `list`

Den mest brugte kollektion. En ordnet række af elementer, som kan ændres.

```python
elever = ["Ida", "Jon", "Kai"]
elever.append("Lea")       # tilføj bagerst
print(elever[0])           # Ida
print(len(elever))         # 4
```

**Brug en liste når:** du har en række ting, hvor rækkefølgen betyder noget, eller hvor der kan være dubletter. Fx en kø, en indkøbsliste, målinger over tid.

### Dictionary – `dict`

En samling af **nøgle–værdi-par**. Man slår en værdi op via dens nøgle – ligesom i en ordbog, hvor man slår et ord op og finder forklaringen.

```python
telefonbog = {"Ida": "22 33 44 55", "Jon": "40 50 60 70"}
print(telefonbog["Ida"])          # 22 33 44 55
telefonbog["Kai"] = "31 31 31 31"  # tilføj nyt par
```

**Brug et dictionary når:** du vil slå noget op ud fra et navn eller en nøgle. Fx postnumre for byer, priser for varer, oplysninger om én elev.

### Tupel – `tuple`

Ligner en liste, men kan **ikke** ændres.

```python
koordinat = (55.68, 12.57)
x, y = koordinat           # "udpakning" af en tupel
```

**Brug en tupel når:** værdierne hører sammen og ikke må ændres. Fx et koordinat, en dato `(2026, 9, 28)`, eller når en funktion skal returnere flere værdier.

### Sæt – `set`

En uordnet samling af **unikke** værdier.

```python
tilmeldte = {"Ida", "Jon", "Ida"}
print(tilmeldte)            # {'Ida', 'Jon'} – dubletten er væk
print("Jon" in tilmeldte)   # True
```

**Brug et sæt når:** du kun interesserer dig for, _om_ noget er med – ikke hvor mange gange eller i hvilken rækkefølge. Fx fjerne dubletter, eller finde fælles elementer i to samlinger.

---

## Hvilken type skal jeg vælge?

Stil dig selv disse spørgsmål – i denne rækkefølge:

1. **Skal jeg slå op via et navn/nøgle?** → `dict`
2. **Må der ikke være dubletter, og er rækkefølgen ligegyldig?** → `set`
3. **Må værdierne aldrig ændres?** → `tuple`
4. **Ellers** → `list`

---

## Fælles for alle fire

Selvom typerne er forskellige, kan man meget af det samme med dem alle:

```python
len(x)          # antal elementer
"Ida" in x      # er "Ida" med? (for dict: er "Ida" en nøgle?)
for e in x:     # gennemløb alle elementer (for dict: alle nøgler)
    print(e)
```

Man kan også **konvertere** mellem typerne med typens navn:

```python
tal = [3, 1, 3, 2]
set(tal)        # {1, 2, 3}  – fjerner dubletter
tuple(tal)      # (3, 1, 3, 2)
list("hej")     # ['h', 'e', 'j']
```

Og man kan **indlejre** dem i hinanden – fx en liste af dictionaries, som er meget almindeligt, når man henter data fra en database eller et API:

```python
elever = [
    {"navn": "Ida", "klasse": "2x"},
    {"navn": "Jon", "klasse": "2y"},
]
print(elever[1]["navn"])    # Jon
```

---

## Ordliste

| Begreb | Forklaring |
|---|---|
| **element** | én værdi i en kollektion |
| **indeks** | positionen af et element – starter ved 0 |
| **nøgle** (key) | det, man slår op med i et dictionary |
| **værdi** (value) | det, der hører til en nøgle |
| **ordnet** | elementerne har en fast rækkefølge |
| **mutable** | kan ændres efter oprettelse |
| **immutable** | kan ikke ændres efter oprettelse |
| **dublet** | samme værdi optræder mere end én gang |
| **iterere / gennemløbe** | gå elementerne igennem ét ad gangen, fx med `for` |
| **slicing** | at tage et udsnit af en liste med `[start:stop:step]` |
