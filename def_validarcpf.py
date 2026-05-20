def validarcpf(cpf):

    if not cpf.isdigit():
        return False

    if len(cpf) != 11:
        return False

    return True