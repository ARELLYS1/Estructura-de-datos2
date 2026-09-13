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