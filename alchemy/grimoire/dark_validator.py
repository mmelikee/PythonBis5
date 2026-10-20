def dark_validate_ingredients(ingredients: str) -> str:
    from .dark_spellbook import dark_spell_allowed_ingredients

    allowed = dark_spell_allowed_ingredients()
    valid = any(item in ingredients.lower() for item in allowed)
    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
