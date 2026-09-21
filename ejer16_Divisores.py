# DIVISORES DE UN NUMERO 

#  Clase DivisorFinder que:
# (1) tenga método encontrar_divisores(numero)
# que retorne una tupla con todos los divisores; 
# (2) tenga método es_perfecto(numero) que retorne True 
# si la suma de sus divisores (excepto él mismo) es igual a él;
# (3) tenga método encontrar_multiples_divisores(*numeros) 
# que retorne un diccionario {número: tupla_divisores}.


class DivisorFinder:

    def encontrar_divisores(self, numero):
        divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)

        return tuple(divisores)

    def es_perfecto(self, numero):
        suma = 0

        for i in range(1, numero):
            if numero % i == 0:
                suma += i

        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)

        return resultado


df = DivisorFinder()

print(df.encontrar_divisores(12))
print(df.es_perfecto(6))
print(df.encontrar_multiples_divisores(6, 10, 12))




#EJERCICIO # 16.1

# FACTORES DE UN NÚMERO

# Clase FactorFinder que:
# (1) tenga método encontrar_factores(numero)
# que retorne una tupla con todos los factores positivos del número;
# (2) tenga método es_primo(numero)
# que retorne True si el número solamente tiene dos factores;
# (3) tenga método encontrar_factores_varios(*numeros)
# que retorne un diccionario {número: tupla_factores}.



class FactorFinder:

    def encontrar_factores(self, numero):
        factores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                factores.append(i)

        return tuple(factores)

    def es_primo(self, numero):
        factores = self.encontrar_factores(numero)

        if len(factores) == 2:
            return True
        else:
            return False

    def encontrar_factores_varios(self, *numeros):
        resultado = {}

        for numero in numeros:
            resultado[numero] = self.encontrar_factores(numero)

        return resultado


# Crear objeto
factor = FactorFinder()

print("Factores de 12:", factor.encontrar_factores(12))

print("¿7 es primo?:", factor.es_primo(7))

print("Factores de varios números:",
      factor.encontrar_factores_varios(6, 10, 15))

