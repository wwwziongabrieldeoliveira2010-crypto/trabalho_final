# =========================

def validar_texto(texto):

    if texto.strip() == "":
        return False

    if any(char.isdigit() for char in texto):
        return False

    return True
