# Módulo: geometria.py
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return area

# programa_principal.py

from geometria import calcular_area_rectangulo, calcular_area_circulo

# Datos para el rectángulo
base_rectangulo = 5
altura_rectangulo = 3
area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
print("El área del rectángulo es:", area_rectangulo)

# Datos para el círculo
radio_circulo = 2
area_circulo = calcular_area_circulo(radio_circulo)
print("El área del círculo es:", area_circulo)