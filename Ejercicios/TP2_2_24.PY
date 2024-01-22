
""" Given a string and a non-empty word string, return a string made of each char just before
    and just after every appearance of the word in the string. Ignore cases where there is no char
    before or after the word, and a char may be included twice if it is between two words.
    Sample: wordEnds("abcXY123XYijk", "XY") → "c13i"

    """
def wordEnds(a, b):
    indice = -1
    lista = []
    lista_a = list(a)
    if b in a: #Saber si la palabra está en la cadena. Si está, la transformo en lista.
        listaA = list(a)
        listaB = list(b)
        for i in lista_a:
            indice += 1
            if i in listaB:
                listaA.remove(i)
                                
    return listaA
print(wordEnds("abcXY123XYijk", "XY"))

 
