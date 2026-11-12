def er_staerk_adgangskode(kode):
    """
    Afgør om en adgangskode er stærk nok.

    En stærk adgangskode skal:
    - være mindst 8 tegn lang
    - indeholde mindst ét ciffer
    - indeholde mindst ét stort bogstav
    - ikke indeholde mellemrum

    Returnerer True hvis adgangskoden er stærk, ellers False.
    """
    if len(kode) < 8:
        return False

    har_ciffer = False
    har_stort_bogstav = False

    for tegn in kode:
        if tegn.isdigit():
            har_ciffer = True
        if tegn.isupper():
            har_stort_bogstav = True
        if tegn == " ":
            return False

    return har_ciffer and har_stort_bogstav


# Manuel test med print
# Du skal selv læse outputtet og vurdere, om resultatet er rigtigt.

if __name__ == "__main__":
    tests = ["Hemmelig1", "Abcdefg1", "Abcdef1", "hemmelig1", "Hemmelig", "Hemm elig1", ""]
    for t in tests:
        print(f"{t!r:14} -> {er_staerk_adgangskode(t)}")
