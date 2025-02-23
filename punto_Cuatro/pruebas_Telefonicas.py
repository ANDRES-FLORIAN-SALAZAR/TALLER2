def validar_telefono(telefono):
    """
    Valida si un número de teléfono tiene el formato +XX-XXX-XXX-XXXX.
    """
    if type(telefono) is not str:
        return False

    partes = telefono.split("-")
    if len(partes) != 4:
        return False

    if not partes[0].startswith("+") or len(partes[0]) != 3:
        return False

    if len(partes[1]) != 3 or len(partes[2]) != 3 or len(partes[3]) != 4:
        return False

    for parte in partes:
        if parte.startswith("+"):
            parte = parte[1:]
        if not parte.isdigit():
            return False

    return True
