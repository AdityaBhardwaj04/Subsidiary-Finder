def normalize_subsidiary_name(name):
    name = name.strip()
    name = name.replace('  ', ' ')

    name = name.lower()

    import re
    name = re.sub(r'[^a-zA-Z0-9 \.]', '', name)

    abbreviations = {
        "Inc": "Incorporated",
        "Ltd": "Limited",
        "Co": "Company"
    }
    for abbr, full_form in abbreviations.items():
        name = name.replace(abbr, full_form)

    return name
