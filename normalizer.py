def normalize_subsidiary_name(name):
    # 1. Basic Cleaning
    name = name.strip()  # Remove leading/trailing whitespace
    name = name.replace('  ', ' ')  # Replace multiple spaces with single spaces

    # 2. Case Normalization (Optional)
    name = name.lower()  # Convert to lowercase (or name.upper() for uppercase)

    # 3. Removing Special Characters (Adjust the pattern as needed)
    import re
    name = re.sub(r'[^a-zA-Z0-9 \.]', '', name)

    # 4. Abbreviation Handling (If applicable)
    abbreviations = {
        "Inc": "Incorporated",
        "Ltd": "Limited",
        "Co": "Company"
        # ... add more as needed
    }
    for abbr, full_form in abbreviations.items():
        name = name.replace(abbr, full_form)

    # ... (Add more normalization rules as needed)

    return name
