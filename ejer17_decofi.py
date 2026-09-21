# CODIFICADOR/ DECODIFICADOR 

# Clase CodificadorCesar que: 
# (1) tenga método codificar_letra(letra, desplazamiento)
# que retorne la letra desplazada en el alfabeto (usar operador %);
# (2) tenga método codificar_palabra(palabra, desplazamiento) 
# que reutilice para toda la palabra; 
# (3) tenga un diccionario como atributo para 
# historial de codificaciones.


class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        codigo = ord(letra)
        nuevo_codigo = ((codigo - ord('a')) + desplazamiento) % 26
        return chr(nuevo_codigo + ord('a'))

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado = resultado + self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


# Ejemplo
cc = CodificadorCesar()

print(cc.codificar_palabra("hola", 3))
print(cc.historial)





# EJERCICIO # 17.1

# Clase CodificadorMensaje que:
# (1) tenga método codificar_letra(letra, desplazamiento)
# que retorne la letra desplazada en el alfabeto usando %;
# (2) tenga método codificar_palabra(palabra, desplazamiento)
# que reutilice codificar_letra() para toda la palabra;
# (3) tenga un diccionario como atributo para guardar
# el historial de codificaciones;
# (4) tenga método decodificar_palabra(palabra, desplazamiento)
# que deshaga la codificación utilizando un desplazamiento negativo;
# (5) tenga método mostrar_historial()
# que retorne todas las palabras codificadas y su resultado.



class CodificadorMensaje:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            inicio = ord('a')
            posicion = ord(letra.lower()) - inicio
            nueva_posicion = (posicion + desplazamiento) % 26
            return chr(inicio + nueva_posicion)
        else:
            return letra

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado

    def decodificar_palabra(self, palabra, desplazamiento):
        return self.codificar_palabra(palabra, -desplazamiento)

    def mostrar_historial(self):
        return self.historial


# Crear objeto
codificador = CodificadorMensaje()


mensaje = codificador.codificar_palabra("hola", 3)
print("Palabra codificada:", mensaje)


original = codificador.decodificar_palabra(mensaje, 3)
print("Palabra decodificada:", original)


print("Historial:", codificador.mostrar_historial())

