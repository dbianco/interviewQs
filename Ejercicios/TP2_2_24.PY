
""" Given a string and a non-empty word string, return a string made of each char just before
    and just after every appearance of the word in the string. Ignore cases where there is no char
    before or after the word, and a char may be included twice if it is between two words.
    Sample: wordEnds("abcXY123XYijk", "XY") → "c13i"

    """
def wordEnds(cadena, palabra):
    indice = -1
    largo= len(palabra)
    if palabra in cadena:
        result = ""
        for i in cadena:
            indice += 1
            if i == palabra[0] and cadena[indice:indice+largo] == palabra:
                result += cadena[indice-1]+cadena[indice+largo]
    return result
print(wordEnds("encuent5aralst7palabra3estuppalabras", "palabra"))

 
