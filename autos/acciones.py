from . import informacion

def conducir():
    return "¡Estás conduciendo el automóvil!"

def calcular_mantenimiento(marca, modelo, año):
    antiguedad = informacion.antiguedad_auto(año)
    if antiguedad <= 3:
        return f"El {marca} {modelo} necesita un mantenimiento básico."
    elif 3 < antiguedad <= 7:
        return f"El {marca} {modelo} requiere un mantenimiento intermedio."
    else:
        return f"El {marca} {modelo} requiere un mantenimiento completo."
