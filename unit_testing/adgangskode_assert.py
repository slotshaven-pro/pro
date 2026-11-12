from adgangskode import er_staerk_adgangskode

# Test med assert
# assert tjekker om en betingelse er True.
# Er den False, stopper programmet med en AssertionError.
# Hvis alle assert-sætninger går igennem, er alle tests bestået.

if __name__ == "__main__":
    # Stærke adgangskoder
    assert er_staerk_adgangskode("Hemmelig1") == True
    assert er_staerk_adgangskode("Abcdefg1") == True, "Præcis 8 tegn skal godkendes"

    # For kort
    assert er_staerk_adgangskode("Abcdef1") == False, "7 tegn er for kort"

    # Mangler stort bogstav
    assert er_staerk_adgangskode("hemmelig1") == False

    # Mangler ciffer
    assert er_staerk_adgangskode("Hemmelig") == False

    # Indeholder mellemrum
    assert er_staerk_adgangskode("Hemm elig1") == False

    # Tom streng
    assert er_staerk_adgangskode("") == False

    print("Alle tests bestået!")
