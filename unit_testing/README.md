# Unit testing i Python

## Hvad er unit testing?

En **unit test** er et lille stykke kode, der tester én enkelt del (en "unit") af dit program – typisk én funktion. Testen kalder funktionen med et bestemt input og tjekker, at resultatet er det, vi forventer.

Hvorfor gøre det?

- **Find fejl tidligt** – du opdager fejlen, mens du stadig husker koden.
- **Tryghed når du ændrer kode** – kør testene igen, og du ved med det samme, om du har ødelagt noget.
- **Dokumentation** – testene viser, hvordan funktionen skal bruges, og hvad den skal returnere.
- **Tænk på grænsetilfælde** – hvad sker der med en tom streng, præcis 8 tegn, et mellemrum?

## Eksemplet: Er adgangskoden stærk nok?

Alle tre eksempler tester funktionen `er_staerk_adgangskode(kode)` i `adgangskode.py`. Den returnerer `True`, hvis adgangskoden er stærk, ellers `False`.

En stærk adgangskode skal:

- være mindst 8 tegn lang
- indeholde mindst ét ciffer
- indeholde mindst ét stort bogstav
- ikke indeholde mellemrum

## Tre måder at teste på

### 1. `adgangskode.py` – manuel test med print

Selve funktionen. Nederst kører vi den på nogle eksempler og **printer** resultatet:

```
python adgangskode.py
```

```
'Hemmelig1'    -> True
'Abcdefg1'     -> True
'Abcdef1'      -> False
...
```

Det virker, men **du** skal selv læse outputtet og vurdere, om det er rigtigt. Det bliver hurtigt uoverskueligt, og det er let at overse en fejl.

### 2. `adgangskode_assert.py` – test med `assert`

Importerer funktionen og tester den med `assert`:

```python
from adgangskode import er_staerk_adgangskode

assert er_staerk_adgangskode("Hemmelig1") == True
assert er_staerk_adgangskode("Abcdef1") == False, "7 tegn er for kort"
```

```
python adgangskode_assert.py
```

Nu er det **computeren**, der tjekker resultatet.

#### Hvad gør `assert`?

`assert` er et nøgleord i Python, der betyder "jeg påstår, at dette er sandt":

```python
assert betingelse
assert betingelse, "besked hvis det ikke er sandt"
```

- Er betingelsen `True`, sker der ingenting – programmet fortsætter.
- Er betingelsen `False`, stopper programmet med en `AssertionError`. Har du skrevet en besked, bliver den vist.

```python
>>> assert 2 + 2 == 4
>>> assert 2 + 2 == 5, "Matematikken er forkert"
AssertionError: Matematikken er forkert
```

Ulempen er, at programmet stopper ved **den første** fejl. Du ser ikke, om andre tests også fejler. Og uden en besked kan det være svært at se, hvad der gik galt.

### 3. `adgangskode_pytest.py` – test med pytest

Importerer funktionen og samler testene i små funktioner, der hver tester én ting:

```python
def test_for_kort():
    assert er_staerk_adgangskode("Abcdef1") == False
```

```
pytest adgangskode_pytest.py -v
```

## Grundlæggende pytest

Installer pytest (én gang):

```
pip install pytest
```

Reglerne er enkle:

- Testfunktioner skal have et navn, der **starter med `test_`**.
- Inde i testen bruger du helt almindelig `assert`.
- Kør `pytest filnavn.py`. Med `-v` (verbose) ser du hver test for sig.
- Kører du bare `pytest` uden filnavn, finder pytest selv alle filer, der hedder `test_*.py` eller `*_test.py`. (Derfor skal `adgangskode_pytest.py` køres med filnavn.)

Output ser sådan ud:

```
adgangskode_pytest.py::test_staerk_adgangskode PASSED
adgangskode_pytest.py::test_praecis_8_tegn PASSED
adgangskode_pytest.py::test_for_kort FAILED
```

Når en test fejler, viser pytest præcis hvilken linje, og hvad værdierne var:

```
>       assert er_staerk_adgangskode("Abcdef1") == False
E       AssertionError: assert True == False
```

**Parametrize** – kør den samme test med mange input:

```python
@pytest.mark.parametrize(
    "kode, forventet",
    [
        ("Hemmelig1", True),
        ("Abcdef1", False),
    ],
)
def test_mange_adgangskoder(kode, forventet):
    assert er_staerk_adgangskode(kode) == forventet
```

Hver linje i listen bliver til sin egen test.

### Hvorfor er pytest den foretrukne måde?

| | `assert` i scriptet | pytest |
|---|---|---|
| Stopper ved første fejl | Ja | Nej – alle tests køres |
| Viser hvilken test der fejlede | Kun hvis du skriver en besked | Ja, med navn |
| Viser hvad værdierne var | Nej | Ja – forventet og faktisk værdi |
| Finder selv testene | Nej | Ja |
| Samme test med mange input | Kopier koden | `parametrize` |

Kort sagt: pytest giver et overblik over **alle** fejl på én gang og forklarer, **hvorfor** en test fejlede. Det er standarden i Python-verdenen.

## Øvelse: Er telefonnummeret gyldigt?

I filen `telefonnummer.py` er der en funktion `valider_telefonnummer(nummer)`. Den returnerer en tuple med tre værdier:

```python
ok, besked, nummer = valider_telefonnummer("12 34 56 78")
# ok     -> True
# besked -> ""
# nummer -> "12345678"
```

Et gyldigt telefonnummer:

- består kun af cifre
- er præcis 8 cifre langt
- må gerne skrives med mellemrum, fx `"12 34 56 78"` (mellemrummene fjernes)

Er nummeret ugyldigt, er `ok` lig med `False`, `besked` forklarer fejlen, og `nummer` er `None`.

**Opgave**

1. Lav en ny fil `test_telefonnummer.py` og importér funktionen:
   ```python
   from telefonnummer import valider_telefonnummer
   ```
2. Skriv testfunktioner, der tjekker:
   - et gyldigt nummer uden mellemrum
   - et gyldigt nummer med mellemrum – bliver mellemrummene fjernet?
   - et nummer med bogstaver
   - en tom streng
   - et nummer, der er for kort
   - et nummer, der er for langt
3. Test ikke kun `ok`, men også `besked` og `nummer`.
4. Kør testene med `pytest -v`.
5. **Der er en fejl i funktionen.** Brug dine tests til at finde den. Ret fejlen i `telefonnummer.py`, og kør testene igen, indtil alle er grønne.

**Ekstra**

- Brug `@pytest.mark.parametrize` til at teste mange telefonnumre i én test.
- Test parametrene `laengde` og `fjern_mellemrum`. Hvad skal der ske med `"12 34 56 78"`, når `fjern_mellemrum=False`?
- Tilføj en ny regel: et nummer må gerne starte med `+45`, fx `"+45 12 34 56 78"`. Skriv testen **først**, se den fejle, og ret så funktionen.
