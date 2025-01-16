def calcular_area_cubo(base, altura, ancho):
    area_cubo = base * altura * ancho
    return area_cubo

def principal():
    base = 5
    altura = 3
    ancho = 7
    resultado = calcular_area_cubo(base, altura, ancho)
    print("El resultado es:", resultado)

principal()
