print("ejemplo de bucles")

valores = [10, 0, 5, "x", 20]

for valor in valores:
    try:
        resultado = 100 / int(valor)
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
        continue
    except ValueError:
        print("Valor no numérico.")
        break