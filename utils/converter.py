PRONOUNS_TO_GENDER = {
    "he/him": "Male",
    "she/her": "Female",
}

VASTAYA_SUBSPECIES = {
    "Vastaya",
    "Besheb",
    "Bryni",
    "Crimson Razorscale",
    "Canghapi",
    "Chyra",
    "Fauhwoon",
    "Juloah",
    "Kepthalla",
    "Khonlui",
    "Kiilash",
    "Lhotlan",
    "Makara",
    "Marai",
    "Oovi-Kat",
    "Ophelis",
    "Ottrani",
    "Raylu",
    "Shimon",
    "Skard",
    "Sodjoko",
    "Strig",
    "Vesani",
    "Vlotah",
    "Vastayan Ancestry"
}

def normalize_gender(pronouns: str) -> str:
    if not pronouns:
        return f"{pronouns} not found!"
    return PRONOUNS_TO_GENDER.get(pronouns.lower().strip(), "Other")

def normalize_species(species: list[str]) -> list[str]:
    normalized = []
    for s in species:
        if s in VASTAYA_SUBSPECIES:
            normalized.append("Vastayan")
        else:
            normalized.append(s)
    return list(set(normalized))
