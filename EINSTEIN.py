#Ejercicio: Que debo hacer para probar la fórmula de la relatividad especial de einstein si quiero, que me calcule dado una masa en kilogramos, cuánta energía tendrá esa masa en Joules

#1. Pedir la masa en kilográmos
masa = int(input("Por favor, ingrese la masa en kilogramos: "))

#2. Calcular la ecuación E=mc**2
c = 300000
energia  = masa * c ** 2

print("La energia en Joules es igual a:", energia, "joules")