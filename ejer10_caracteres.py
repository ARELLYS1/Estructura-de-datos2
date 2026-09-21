# VALIDADOR DE CARACTERES 

#Clase AnalizadorString que: 
# (1) tenga método solo_vocales(letra) que retorne True si es vocal; 
# (2) tenga método contar_por_tipo(texto) que retorne un diccionario
# {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos;
# (3) tenga atributo que guarde el texto más largo analizado.


class AnalizadorString:

    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        vocales = 0
        consonantes = 0
        digitos = 0

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        for letra in texto:
            if self.solo_vocales(letra):
                vocales += 1
            elif letra.isdigit():
                digitos += 1
            elif letra.isalpha():
                consonantes += 1

        return {
            "vocales": vocales,
            "consonantes": consonantes,
            "digitos": digitos
        }



astr = AnalizadorString()


print(astr.contar_por_tipo("Hola123"))


print("Texto más largo:", astr.texto_mas_largo)




#EJERCICIO 10.1
#ANALIZADOR DE PALABRAS
# Crear una clase AnalizadorPalabras 
#Tenga un atributo que guarde la palabra más larga analizada.
# Tenga un método es_mayuscula(letra) que retorne True si la letra está en mayúscula.
# Tenga un método analizar_texto(texto) que retorne un diccionario:

class AnalizadorPalabras:

    def __init__(self):
        self.palabra_mas_larga = ""

    def es_mayuscula(self, letra):
        return letra.isupper()

    def analizar_texto(self, texto):
        mayusculas = 0
        minusculas = 0
        espacios = 0

        palabras = texto.split()

        for palabra in palabras:
            if len(palabra) > len(self.palabra_mas_larga):
                self.palabra_mas_larga = palabra

        for letra in texto:
            if self.es_mayuscula(letra):
                mayusculas += 1
            elif letra.islower():
                minusculas += 1
            elif letra == " ":
                espacios += 1

        return {
            "mayusculas": mayusculas,
            "minusculas": minusculas,
            "espacios": espacios
        }


ap = AnalizadorPalabras()

print(ap.analizar_texto("Hola Mundo Python"))

print("Palabra más larga:", ap.palabra_mas_larga)