def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    return palabra == palabra_invertida


palabra_usuario = input(" ingrese una palabra: ")


if es_palindromo(palabra_usuario):
    
     print("la palabra", palabra_usuario, "es palíndromo")

else:

     print("la palabra", palabra_usuario, "no es palíndromo")
