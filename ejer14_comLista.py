#  COMBINADOR DE LISTAS 

#  Clase CombinadorListas que: (1) tenga método intercalar(lista1, lista2)
# que retorne una lista alternando elementos de ambas; 
# (2) tenga método intercalar_multiples(*listas) 
# que reutilice para varias listas.



class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []
        
        mayor = max(len(lista1), len(lista2))

        for i in range(mayor):
            if i < len(lista1):
                resultado.append(lista1[i])

            if i < len(lista2):
                resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []
        
        mayor = 0

        for lista in listas:
            if len(lista) > mayor:
                mayor = len(lista)

        for i in range(mayor):
            for lista in listas:
                if i < len(lista):
                    resultado.append(lista[i])

        return resultado


cl = CombinadorListas()

print(cl.intercalar([1, 2], [3, 4]))

print(cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))