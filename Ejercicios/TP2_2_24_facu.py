def char_after_before(cadena, letras):
    n = len(letras) #valor 2
    contador = 0
    result = ""
    # print(cadena[3:4])
    # print(cadena[8:10])
    # print(cadena[5])
    for let in cadena:
        if  let == letras[0]: #si la letra es igual a la primera letra de "letras"
            indice = contador #indice es cero (valor del contador)
            
            if letras == cadena[indice:(indice + n)]: #cadena[3:5] cadena (8:10)
                result += cadena[indice - 1] #cadena [2]
                result += cadena[indice + 1 + (n - 1)]#cadena[5]
                '''n-1 da la cantidad de indices. Si la cadena iene 8 caracteres, 
                tiene indice  de 0 a 7. sería: 3+1 + (2-1)'''
        contador += 1
    return result

print(char_after_before("abcXY123XYijk", "XY"))
