---
subject: Programmering B
description:
---

# Validering af telefonnummer

Øvelse med funktioner.

I det følgende skal du udvikle en funktion, `validate_phone_number()`, der validerer et telefonnummer. Funktionen bliver
trinvist forbedret efterhånden som kravene bliver højere.

Funktionen skal

- have telefonnummeret som parameter
- returnere resultatet af valideringen (True/False til at begynde med)
- have en docstring som dokumenterer hvad funktionen gør

Du kan bruge denne kode som udgangspunkt:

```python
def validate_phone_number(phone_number):
    """ Min telefonnummervalideringsfunktion """
    # valider phone_number her
    return False  # skal ændres
```

Alle dine funktioner skal altid testes (se nedenfor).

Slet ikke de forskellige versioner som du laver undervejs – kopiér dem og byg videre på dem i næste opgave.

**Besvarelse i `.py`-script**:
Når du besvarer opgaven i et Python-script, giv din funktion nummer efter
opgaven, fx `validate_phone_number_1()`.

Vis altid et eksempel på brug af funktionen (input/output).

For at teste din funktion, kan du indsætte denne kodeblok nederst i dit script, som tester numrene i listen.
```python
if __name__ == "__main__":
    tests = ["12345678", "12 34 56 78", " 1234 5678 ", "1234567", "1234abcd", ""]

    print("Resultat: Udgave 1:")  # ret udgavenummeret
    for tlf in tests:
        resultat = validate_phone_number(tlf)  # ret funktionsnavnet, fx validate_phone_number_1
        print(f"  '{tlf}' -> {resultat}")
```

**Besvarelse i notebook**:
Hvis du bruger en notebook, så lav en ny kodecelle til hver opgave.
Her behøver du ikke at give funktionen nyt navn hver gang.

Igen: husk at teste funktionen.

## Opgave 1. Er det gyldigt?

Første udgave af funktionen skal validere, at telefonnummeret:

- er 8 tegn langt
- kun består af cifre

Funktionen skal returnere True hvis nummeret er korrekt, ellers False.

## Opgave 2. Fjern whitespace

Hvad sker der, når funktionen validerer et nummer som "12 34 56 78"? Er det gyldigt?

Lav en ny udgave af din funktion som fjerner mellemrum (whitespace), før den validerer.

Tip:

```python
res = "22 33 44 55".split() # giver ['22','33','44','55']
"".join(['A', 'B', 'C']) # giver "ABC"
```

Læs mere [her (split)](https://www.w3schools.com/python/ref_string_split.asp) og [her (join)](https://www.w3schools.com/python/ref_string_join.asp)

## Opgave 3. Ny parameter: antallet af cifre

Nu skal vi gøre vores funktion mere anvendelig ved hjælp af parametre.

Tilføj en parameter, `no_of_digits`, så man kan angive antallet af cifre.
Lav en ny version af din kode, så den bruger det nye parameter.

## Opgave 4. Ny parameter: fjern whitespace

Tilføj en parameter, `remove_whitespace`, som styrer om whitespace skal fjernes eller ej.
Skriv din kode om så den bruger dette nye parameter.

## Opgave 5. Standardværdier

Giv de to nye parametre i de forrige opgaver fornuftige standardværdier (default-værdier).

Hvad er fornuftige standardværdier i dette tilfælde?

## Opgave 6. Fejlbesked

Nu skal funktionen returnere en relevant fejlbesked, hvis nummeret har et ugyldigt format.

Fx `Ugyldigt telefonnummer: må kun indeholde tal.` eller `Ugyldigt telefonnummer: skal indeholde 8 cifre.`.

Brug `no_of_digits` i fejlbeskeden, så antallet af cifre altid passer.

Man kan returnere flere værdier fra en funktion sådan her:

```python
return False, 'Ugyldigt telefonnummer: må kun indeholde tal.'
# eller
return True, 'Gyldigt format'
```

Bemærk! Når vi ændrer returværdien, skal vi også ændre vores testkode. Nu kommer der pludselig
**to** værdier tilbage – som en tupel (typen `tuple`).

Det kan vi gemme i to variable sådan her:
```python
status, error_message = validate_phone_number( ... )
```

## Opgave 7. Returnér det formaterede nummer

Hvis der er fjernet whitespace fra det oprindelige telefonnummer, vil kalderen (den linje kode som kaldte
funktionen) gerne have det formaterede nummer tilbage i returværdien.
Tilføj nu det formaterede nummer til returværdien, så der returneres en tupel med tre værdier.
Returnér altid nummeret, som det ser ud efter en evt. rensning – også selvom der ikke er fjernet noget.

Argh – husk at så skal man omskrive testkoden endnu en gang for nu kommer der **tre** værdier tilbage.


## Ekstraopgave 8. Landekode

Hvad hvis vi gerne vil acceptere numre med landekode, som fx "+45 21436587"?

Kan du skrive din funktion, så den kan acceptere numre med landekode?

[Måske er der hjælp at hente her?](https://www.w3schools.com/python/ref_string_startswith.asp)
