def ordenar_rapido(lista):
    if len (lista) <=1:
        return lista
    
    pivote = lista [-1]

    menores = [elemento for elemento in lista[:-1] if elemento <= pivote]
    mayores = [elemento for elemento in lista[:-1] if elemento > pivote]

    menores_ordenados = ordenar_rapido(menores)
    mayores_ordenados = ordenar_rapido(mayores)

    return menores_ordenados + [pivote] + mayores_ordenados

lista = [3,4,7,8,5,2,6]
print ("lista_original:", lista)
lista_ordenada = ordenar_rapido(lista)
print ("lista_ordenada:", lista_ordenada)




    
