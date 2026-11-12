import pytest

from adgangskode import er_staerk_adgangskode

# Test med pytest
# Kør i terminalen:  pytest adgangskode_pytest.py -v
# pytest finder selv alle funktioner, hvis navn starter med test_


def test_staerk_adgangskode():
    assert er_staerk_adgangskode("Hemmelig1") == True


def test_praecis_8_tegn():
    assert er_staerk_adgangskode("Abcdefg1") == True


def test_for_kort():
    assert er_staerk_adgangskode("Abcdef1") == False


def test_mangler_stort_bogstav():
    assert er_staerk_adgangskode("hemmelig1") == False


def test_mangler_ciffer():
    assert er_staerk_adgangskode("Hemmelig") == False


def test_mellemrum():
    assert er_staerk_adgangskode("Hemm elig1") == False


def test_tom_streng():
    assert er_staerk_adgangskode("") == False


# Samme test kørt med mange forskellige input på én gang
@pytest.mark.parametrize(
    "kode, forventet",
    [
        ("Hemmelig1", True),
        ("Abcdefg1", True),
        ("SUPERHEMMELIG2026", True),
        ("Abcdef1", False),
        ("hemmelig1", False),
        ("Hemmelig", False),
        ("Hemm elig1", False),
        ("12345678", False),
        ("", False),
    ],
)
def test_mange_adgangskoder(kode, forventet):
    assert er_staerk_adgangskode(kode) == forventet
