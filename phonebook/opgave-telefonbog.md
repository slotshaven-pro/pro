# Forløb: Telefonbog

I dette forløb skal du bygge et program, som fungerer som en **telefonbog**.  

Programmet bruger et **dictionary** til at gemme navne og telefonnumre, og **funktioner** til at udføre de forskellige handlinger.  

- Brug dictionaries til at håndtere data  
- brug funktioner til at organisere programmet  

I forløbet anvender vi desuden en lang række centrale begreber og teknikker fra programmering:

- pseudokode
- moduler
- automatiseret test 
- filhåndtering
- dokumentation
- overførsel af parametre fra kommandolinjen 

## Opgave. Basal funktionalitet

Den første version af programmet skal kunne:

1. **Tilføje en ny kontakt** (brugeren indtaster navn og telefonnummer)  
2. **Finde et telefonnummer** ud fra et navn  
3. **Vise alle kontakter**  
4. **Afslutte programmet**

Alle fire menupunkter skal udføres via **funktioner**.  
Brugeren skal vælge, hvad de vil gøre, via et menu-system.


### Eksempeldata

Start fx med et dictionary med tre eksempler på kontakter.

```python
contacts = {
    "Anna": "23456789",
    "Bjørn": "99887766",
    "Clara": "11223344"
}
```
### Skriv funktionerne

Brugeren skal kunne vælge mellem mulighederne via `input()`.  

Sådan kunne dit main loop se ud:

```python
# Sådan kunne dit main loop se ud
while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        # indtast kontakt
        name, phone_no = get_contact()
        # tilføj kontakt med funktion
        add_contact(name, phone_no)

    # etc. 
    if choice == "4":
        goodbye() # Kald din luk-ned-funktion
        exit()
```
Programmet skal have funktioner til at håndtere hvert menupunkt.  
Skriv disse funktioner.

Husk at dokumentere funktionerne med _docstrings_. 

Beskriv: 

- hvad funktionen gør
- hvad parametrene gør
- hvad funktionen returnerer

```python
def add_contact(name, phone_no):
    """ 
     Tilføjer name og phone_no til telefonbog.
     Hvis navn eksisterer i forvejen, udskrives fejlmeddelelse. 
     Return sandt hvis operationen lykkedes, ellers falsk.
    """
```

Alle funktioner skal definere et eller to parametre.

## Opgave. Gem telefonbogen i en fil

Det er irriterende at alle kontakter forsvinder, hver gang programmet lukkes.
Nu skal du udvide programmet, så telefonbogen kan gemmes og læses fra en fil.

Man kan bruge modulet `json`, som kan gemme og læse dictionaries direkte til og fra tekstfiler.
Data bliver gemt som i formatet `json`.

### Gem telefonbogen i en fil

```python
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)
```

### Læs telefonbogen fra en fil

```python
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
```

Tilføj nogle to funktioner til dit program som indlæser dine kontakter når programmet starter og gemmer dem når programmet afsluttes.

**Bemærk:**

- `with open(...)` sørger for, at filen automatisk bliver lukket igen.
- `"w"` betyder *write* (overskriver filen), `"r"` betyder *read*.
- `encoding="utf-8"` og `ensure_ascii=False` gør, at æ, ø og å gemmes korrekt.

**Ekstra:** Gem telefonbogen hver gang en kontakt tilføjes, så intet går tabt, hvis programmet går ned.

## Opgave. Validering af telefonnummer

Denne opgave falder i to dele: 

- pseudokode
- implementering

**Pseudokode**:

Overvej hvad kravene til et gyldigt nummer er. Et par forslag:

- 8 tegn langt
- består kun af cifre

**Validering af telefonnummer**:

Skriv en funktion som validerer (kontrollerer) formatet på et telefonnummer
som du har specificeret den i din pseudokode. 

## Opgave. Automatiseret test 

Skriv en automatiseret test af din valideringsfunktion. 

Den kan skrives med `pytest`.


## Opgave. Kommandolinje

Gør dit program klar til at modtage parametre på kommandolinjen. 


 