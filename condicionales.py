print("ejemplos de condicionales")

def procesar_dato(dato):
    match dato:
        case {"tipo": "texto", "valor": str(valor)}:
            return f"Texto recibido: {valor}"
        case {"tipo": "numero", "valor": int(valor)}:
            return f"Número al cuadrado: {valor ** 2}"
        case _:
            return "Tipo desconocido"

