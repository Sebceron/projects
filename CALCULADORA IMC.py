peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
   resultado = "Bajo peso"
elif imc < 25:
   resultado = "Peso Normal"
else:
   resultado = "Sobre peso"

print(f"su IMC es {imc:.1f}. Usted tiene {resultado}. ")