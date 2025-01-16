# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(altura, base):
    area = altura * base
    return area

# Función para calcular el área de un triángulo
def calcualar_area_triangulo(base,altura):
    area_triangulo = 0.5 * base * altura
    return area_triangulo

# Función principal
def main():
    altura = 4
    base = 6
    rectangulo_area = calcular_area_rectangulo(altura, base)
    print("Área del rectángulo:", rectangulo_area)

    base = 5
    altura = 8
    triangulo_area = calcualar_area_triangulo(base,altura)
    print("Área del triángulo:", triangulo_area)

main()
