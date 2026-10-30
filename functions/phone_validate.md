# Validering af telefonnummer

Skriv en funktion, der validerer et telefonnummer.

Når du besvarer opgaven, giv din funktion nummer efter opgaven, fx `validering_1()`.
Når du besvarer opgaven, giv altid kodeeksempler på hvordan funktionen bruges.

## Opgave 1

Skriv en funktion der validerer at telefonnummeret er:

- 8 tegn langt
- kun består af cifre
- ikke indeholder whitespace

Funktionen returner True hvis nummeret er korrekt, ellers False.

## Opgave 2

Tilføj parametre til din nye funktion.

Tilføj et parameter, så man kan angive antallet af cifre. Giv paremeteret en default på 8.
Tilføj parameter som styrer om whitespace skal fjernes eller ej.

Skriv koden så den bruger de nye parametre.


```python
if __name__ == "__main__":
    tests = ["12345678", "12 34 56 78", " 1234 5678 ", "1234567", "1234abcd", ""]

    print("Udgave 1:")
    for t in tests:
        print(f"  {t} -> {validate_phone_number(t)}")
```

## Opgave 3

Nu skal du returne en relevant fejlbesked,  hvis nummeret har et ugyldigt format.

Fx `Nummeret må indeholde tal` eller `Længden skal være 8`.

Man kan returnere flere værdier fra en funktion sådan her
```python
return False, 'Ugyldigt telefonnummer: må kun indeholde tal.'

return True, 'Gyldigt format'
```
