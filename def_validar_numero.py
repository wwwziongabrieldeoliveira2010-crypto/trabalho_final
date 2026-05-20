def validar_numero(numero):

    if numero.strip() == "":
        return False

    try:
        float(numero)
        return True

    except:
        return False
