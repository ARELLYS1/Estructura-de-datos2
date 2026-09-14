#  EJERCIO_1 contar del 1 al N 

# Leer un número N y mostrar los números del 1 al N.

# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # n (entero)
   
   # 2 proceso - que hago con eso 
   # recorrer desde 1 hasta N con un for
   
   # 3 Salida - Què debo mostrar 
   # los N números uno por línea
   
# 2) BOSQUEJO A MANO 
   # n = 5

   # for i in range (1, 6):  # 1, 2, 3, 4, 5
   # print(i)
   
# 3) DESCUBRIR EL PATRÒN 
  # Tabla de decisión del range:

  # Si quiero contar del 1 al N, uso range(1, N+1).
  # El segundo número es exclusivo: range(1, 6) da 1, 2, 3, 4, 5, no llega a 6.
  # El error clásico es escribir range(1, N): te falta el último número.
  
# 4) ESCRIBIR EL CODIGO 

n = int(input("N: "))

print("Ascendente:")

for i in range(1, n + 1):
    print(i)

print("Descendente:")

for i in range(n, 0, -1):
    print(i)
    
    
    
#  EJERCIO_2 SUMA DE LOS PRIMEROS N NATURALES

# Leer N y calcular la suma de 1 + 2 + 3 + ... + N.

# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # n (entero)
   
   # 2 proceso - que hago con eso 
   # Acumular en una variable con un bucle
   
   # 3 Salida - Què debo mostrar 
   # la suma total
   
# 2) BOSQUEJO A MANO 
   # n = 5,     suma = 0 (INICIALIZACIÓN)

   # fi=1:  suma = 0 + 1 = 1
   # i=2:  suma = 1 + 2 = 3
   # i=3:  suma = 3 + 3 = 6
   # i=4:  suma = 6 + 4 = 10
   # i=5:  suma = 10 + 5 = 15   ← resultado
   
# 3) DESCUBRIR EL PATRÒN 

  # Aquí aparece el patrón acumulador: una variable
  # (suma) que se va aumentando dentro del bucle.
  # La regla de oro del acumulador: inicializarlo 
  # en 0 si vas a sumar, en 1 si vas a multiplicar.
  # Y siempre fuera del bucle, porque si lo pones dentro, en cada vuelta lo reseteas.
  # Curiosidad: Python tiene sum(range(1, n+1)) 
  # que hace lo mismo en una línea. Pero como estamos 
  # aprendiendo, usamos el bucle explícito.
  
  
# 4) ESCRIBIR EL CODIGO 

n = int(input("n: "))

# Suma del 1 hasta n
suma = 0

for i in range(1, n + 1):
    suma += i

print(f"La suma del 1 hasta {n}: {suma}")


# Suma de los pares del 2 al 100
suma_pares = 0

for i in range(2, 101, 2):
    suma_pares += i

print(f"La suma de los pares del 2 al 100: {suma_pares}")

  
    
#  EJERCIO_3 FACTORIAL DE N 

# Leer N y calcular el factorial (N! = 1 × 2 × 3 × ... × N). Ejemplo: 5! = 120.

# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # n (entero)
   
   # 2 proceso - que hago con eso 
   # Acumulador multiplicativo
   
   # 3 Salida - Què debo mostrar 
   # El factorial 
   
# 2) BOSQUEJO A MANO 
   # n = 5,     suma = 0 (INICIALIZACIÓN)

   # n = 5, fact = 1 (INICIALIZACIÓN)

   # i=1:  fact = 1 * 1 = 1
   # i=2:  fact = 1 * 2 = 2
   # i=3:  fact = 2 * 3 = 6
   # i=4:  fact = 6 * 4 = 24
   # i=5:  fact = 24 * 5 = 120   ← resultado
   
# 3) DESCUBRIR EL PATRÒN 

  # Mismo patrón que el ejercicio anterior, 
  # pero multiplicativo. Lo que cambia es la inicialización: 
  # si empiezas en 0, todo el resultado será 0 
  # (porque cualquier cosa × 0 = 0). Empezar en 1 es la clave.
  # Regla: elemento neutro — 0 para la suma (n + 0 = n),
  # 1 para la multiplicación (n × 1 = n).
  
  
# 4) ESCRIBIR EL CODIGO 
  
  
n= int(input("N: "))
fact = 1

for i in range(1, n + 1 ):
    fact = fact * i
    
    print(f"el factorial: {fact}")
    
    
    
# opcion 
# ¿Qué pasa con N muy grande (100!)? 
# Python maneja enteros infinitos, pruébalo. 
# En JS con enteros normales explotaría.


n = int(input("N: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"El factorial: {fact}")
  
  
  
#  EJERCIO_4 CUANTOS APROBARON

# Leer las notas de N estudiantes (una por una
# ) y contar cuántos aprobaron (nota ≥ 70).

# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # n (cantidad) y n notas 
   
   # 2 proceso - que hago con eso 
   # recorrer con for y contar con un contador
   
   # 3 Salida - Què debo mostrar 
   # cuántos tienen nota ≥ 70

   
# 2) BOSQUEJO A MANO 
   # n = 4, aprobados = 0 (INICIALIZACIÓN)

   # nota=8 → 8 >= 7 → aprobados = 1
   # nota=5 → 5 >= 7 → NO cambia
   # nota=9 → 9 >= 7 → aprobados = 2
   # nota=6 → 6 >= 7 → NO cambia

   # resultado: 2 aprobados

# 3) DESCUBRIR EL PATRÒN 

  # Aquí aparece el patrón contador: 
  # como el acumulador, pero solo suma 1 cuando pasa algo.
  # Se combina con un if dentro del bucle.

  # Fíjate que hay dos bucles imaginarios juntos: 
  # (1) uno que lee las N notas, (2) dentro del cuerpo, 
  # un if que decide si aumentar el contador.
  
# 4) ESCRIBIR EL CODIGO 

n = int(input("¿Cuántos estudiantes? "))
aprobados = 0                       
for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota >= 7:                    
        aprobados += 1              

print(f"Aprobados: {aprobados} de {n}")


# opcion

n = int(input("¿Cuántos estudiantes? "))

aprobados = 0
reprobados = 0

for i in range(n):

    nota = float(input(f"Nota {i+1}: "))

    if nota >= 7:
        aprobados += 1
    else:
        reprobados += 1

porcentaje = (aprobados / n) * 100

print(f"Aprobados: {aprobados} de {n}")
print(f"Reprobados: {reprobados} de {n}")
print(f"Porcentaje de aprobación: {porcentaje}%")
  
  
  
#  EJERCIO_5 LA NOTA MAS ALTA (PATRON CAMPEON )
  
# Leer las notas de N estudiantes y mostrar la nota más alta.


# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # n y las n notas 
   
   # 2 proceso - que hago con eso 
   # guardar la nota más alta encontrada hasta ahora, 
   # actualizarla si aparece una mayor
   
   # 3 Salida - Què debo mostrar 
   # la nota más alta

   
# 2) BOSQUEJO A MANO 
   # nota máxima = -infinito (o = primera nota)

   # leo 6  → 6 > -inf → máx = 6
   # leo 9  → 9 > 6   → máx = 9
   # leo 4  → 4 > 9   → NO cambia
   # leo 8  → 8 > 9   → NO cambia
   # leo 10 → 10 > 9  → máx = 10

   # resultado: 10


# 3) DESCUBRIR EL PATRÒN 

  # Patrón campeón (o mayor). Guardas la mejor nota vista hasta 
  # ese momento y la actualizas cuando aparece una mayor.
  # El problema es cómo inicializar. Dos opciones:

  #  Con la primera nota leída (mejor): el bucle empieza en el segundo dato.
  # Con un valor imposible (float negativo infinito): el bucle empieza en el primero.

  # Aquí usamos la segunda porque queda más limpia con range(n).
  
  
# 4) ESCRIBIR EL CODIGO 

n = int(input("¿Cuántas notas? "))
maxima = float("-inf")              

for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    if nota > maxima:               
        maxima = nota             

print(f"Máxima: {maxima}")


# opcion 


n = int(input("¿Cuántas notas? "))

minima = float("inf")

for i in range(n):

    nota = float(input(f"Nota {i+1}: "))

    if nota < minima:
        minima = nota

print(f"Mínima: {minima}")



# EJERCIO_6 ¿ES PRIMO?
  
# Leer un número y determinar 
# si es primo (solo divisible entre 1 y él mismo).


# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # n (entero)
   
   # 2 proceso - que hago con eso 
   # probar divisores de 2 hasta √n usando bandera
   
   # 3 Salida - Què debo mostrar 
   # "n es primo" o "n no es primo"

   
# 2) BOSQUEJO A MANO 
   # n = 17, es_primo = True (bandera)

   # Pruebo divisores del 2 al √17 ≈ 4:
   # 17 % 2 = 1 (no divide)
   # 17 % 3 = 2 (no divide)
   # 17 % 4 = 1 (no divide)

   # Ninguno dividió → 17 es primo ✓


# 3) DESCUBRIR EL PATRÒN 

  #Aquí usamos el patrón bandera: una variable booleana que
  # empieza en True y cambia a False apenas se descarta.

  # Optimización clave: solo hace falta probar hasta √n, 
  # no hasta n. Si n tiene un divisor mayor que √n, forzosamente
  # tiene otro menor que ya habríamos encontrado.

  # Un caso especial: 0 y 1 no son primos. Se descarta al inicio.
  
  
# 4) ESCRIBIR EL CODIGO 

n = int(input("Número: "))
es_primo = True                   

if n < 2:
    es_primo = False                
else:
    # Probar divisores del 2 hasta √n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:              
            es_primo = False        
            break                   

if es_primo:
    print(f"{n} es primo")
else:
    print(f"{n} NO es primo")
    
    
    
# opcion 


primos = []

for n in range(2, 101):

    es_primo = True

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            es_primo = False
            break

    if es_primo:
        primos.append(n)

print(f"Primos: {primos}")



# EJERCIO_7 TABLA DE MULTIPLICAR 
  
# Lee un número N y muestra su tabla de multiplicar (del 1 al 12).


# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # n (entero)
   
   # 2 proceso - que hago con eso 
   # Debemos multiplicar el número N por cada número desde 1 hasta 12.
   
   # 3 Salida - Què debo mostrar 
   # Mostrar la tabla de multiplicar

   
# 2) BOSQUEJO A MANO 
   #N = 5

   # 5 × 1 = 5
   # 5 × 2 = 10
   # 5 × 3 = 15
   # 5 × 4 = 20
   # 5 × 5 = 25
   # 5 × 6 = 30
   # 5 × 7 = 35
   # 5 × 8 = 40
   # 5 × 9 = 45
   # 5 × 10 = 50
   # 5 × 11 = 55
   # 5 × 12 = 60

# 3) DESCUBRIR EL PATRÒN 

  # AObservamos que:

  # El número N siempre es el mismo.
  # El segundo número comienza en 1.
  # Va aumentando de 1 en 1.
  # Termina en 12.
  # La operación que se repite es una multiplicación.
  
  
# 4) ESCRIBIR EL CODIGO 

n = int(input("Número: "))

for i in range(1, 13):
    resultado = n * i
    print(f"{n} x {i} = {resultado}") 
    
    
    
# EJERCIO_8 CONTAR DIGITOS DE UN NUMERO 
  
# Lee un número y cuenta cuántos dígitos tiene (sin convertir a string).


# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # n (entero)
   
   # 2 proceso - que hago con eso 
   # Tenemos que contar cuántos dígitos tiene sin convertirlo a texto.
   # Para hacerlo, dividimos el número entre 10 usando división entera:
   # 4567 → 456 → 45 → 4 → 0
   # Cada división elimina un dígito.
   #Por cada vez que hacemos esto, aumentamos un contador.
   
   # 3 Salida - Què debo mostrar 
   # Los numeros de digitos que tiene el numero ingresado

   
# 2) BOSQUEJO A MANO 
   # n = 4567
   # contador = 0

# 3) DESCUBRIR EL PATRÒN 

  # AObservamos que:

  # n = n // 10
  # Y cada vez aumentamos:
  # contador = contador + 1
  # Mientras n sea diferente de 0, seguimos repitiendo.
  
  
# 4) ESCRIBIR EL CODIGO 

n = int(input("Número: "))

contador = 0

while n != 0:
    n = n // 10
    contador += 1

print(f"Cantidad de dígitos: {contador}")




# EJERCIO_9 SUMA DE PARES E IMPARES 
  
# Lee N números y muestra la suma de los pares
# y la suma de los impares por separado.


# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # Primero preguntamos cuántos números se van a ingresar.
   
   # 2 proceso - que hago con eso 
   
   # Tenemos que separar los números en:
   # Pares: se pueden dividir entre 2 exactamente.
   # Impares: no se pueden dividir entre 2 exactamente.
   # Luego sumamos cada grupo por separado.
   
   
   # 3 Salida - Què debo mostrar 
   # la suma de los pares y la suma de los imapres 

   
# 2) BOSQUEJO A MANO 
   # n=5 

  # Número     Tipo       Suma
  # 2          Par        2
  # 7          Impar      7
  # 4          Par        6
  # 9          Impar      16
  # 6          Par        12
    
  # Suma pares = 12
  # Suma impares = 16
  
  
# 3) DESCUBRIR EL PATRÒN 

  # Vemos que debemos repetir el proceso N veces.
  # Necesitamos dos variables para guardar las sumas:
  # suma_pares = 0
  # suma_impares = 0

  
  
# 4) ESCRIBIR EL CODIGO 

n = int(input("¿Cuántos números? "))
suma_pares = 0
suma_impares = 0

for i in range(n):
    x = int(input(f"Número {i+1}: "))
    if x % 2 == 0:
        suma_pares += x
    else:
        suma_impares += x

print(f"Suma pares: {suma_pares}")
print(f"Suma impares: {suma_impares}")
    
    
    
    
# EJERCIO_10 VALIDAR ENTRADA ( BUCLE CON CENTINELA)
  
# Pide una edad y valida que esté entre 0 y 120. 
# Si el usuario ingresa algo inválido, vuelve a pedirla.


# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # n (entero)
   
   # 2 proceso - que hago con eso 
   
   # Tenemos que comprobar si la edad es válida.
   # Si está entre 0 y 120 → es válida.
   # Si es menor que 0 o mayor que 120 → es inválida y se vuelve a pedir.
   # Como necesitamos repetir hasta que sea válida, usamos un while.
   
   
   # 3 Salida - Què debo mostrar 
   
   # Muestra si la edad es valida o invalida 

   
# 2) BOSQUEJO A MANO 
   # edad = 150
   # 150 >= 0 → Sí
   # 150 <= 120 → No
   # Edad inválida → pedir nuevamente.
   # edad = 25
   # 25 >= 0 → Sí
   # 25 <= 120 → Sí
   # Edad válida → terminar.

  
# 3) DESCUBRIR EL PATRÒN 

  # Mientras la edad sea menor que 0 O mayor que 120:
  # pedir nuevamente la edad
  # Cuando la edad esté dentro del rango, el ciclo termina.
  
# 4) ESCRIBIR EL CODIGO 
    
while True:
    edad = int(input("Edad (0-120): "))
    if 0 <= edad <= 120:
        break                       # sale del while
    print("Inválida, intenta de nuevo")

print(f"Edad válida: {edad}")





# EJERCIO_11 ADIVINA EL NUMERO 
  
# Genera un número secreto entre 1 y 100. 
# El usuario intenta adivinar. En cada intento le dices 
# si es «mayor» o «menor». Cuenta cuántos intentos usó.

# 1) ENTENDER EL PROBLEMA 

   # 1 ENTRADA - QUÈ ME DAN 
   
   # El programa genera un número secreto entre 1 y 100.
   # Luego el usuario ingresa números intentando adivinarlo.
   
   # 2 proceso - que hago con eso 
   
   # En cada intento:
   # Si el número ingresado es menor que el secreto → mostrar "Mayor".
   # Si el número ingresado es mayor que el secreto → mostrar "Menor".
   # Si es igual → mostrar que acertó.
   # Contamos cada intento.
   
   
   # 3 Salida - Què debo mostrar 
   
   # el numero adivinado ya sea mayor o menor 

   
# 2) BOSQUEJO A MANO 
   # Secreto = 50
   # Intentos = 0
 
   # Usuario: 30
   # 30 < 50 → Mayor
   # Intentos = 1

   # Usuario: 70
   # 70 > 50 → Menor
   # Intentos = 2

   # Usuario: 50
   # 50 == 50 → Correcto
   # Intentos = 3
   
   
# 3) DESCUBRIR EL PATRÒN 

  # El patrón es repetir los intentos hasta que el usuario encuentre el número secreto.
  # Necesitamos:
  # secreto → número aleatorio
  # intentos → contador
  # while → repetir intentos
  # if → comparar números
  
  
# 4) ESCRIBIR EL CODIGO 
    
    
import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina (1-100): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Es mayor")
    else:
        print("Es menor")






# EJERCIO_12 SERIE DE FIBONACCI
  
# Muestra los primeros N números de Fibonacci.
# La serie: 0, 1, 1, 2, 3, 5, 8, 13, 21... 
# Cada número es la suma de los dos anteriores.


# 1) ENTENDER EL PROBLEMA 

   # 1 ENTRADA - QUÈ ME DAN 
   
   # Pedimos al usuario cuántos números de Fibonacci quiere mostrar.
   # Ejemplo:
   # N = 8
   
   # 2 proceso - que hago con eso 
   
   # Comenzamos con dos números:
   # a = 0
   # b = 1
   # Despues, cada numero nuevo se obtiene sumando los dos anteriores 
   # 0 + 1 = 1
   # 1 + 1 = 2
   # 1 + 2 = 3
   # 2 + 3 = 5


   # 3 Salida - Què debo mostrar 
   
   # Mostrar los primeros numeros de fibonacci

   
# 2) BOSQUEJO A MANO 

   # N = 6
   # a = 0
   # b = 1
   
   # vuelta     a         b 
   # 1          0         1
   # 2          1         1
   # 3          1         2
   # 4          2         3
   # 5          3         5
   # 6          5         8
   
   # resultado:  0, 1, 1, 2, 3, 5
   
   
# 3) DESCUBRIR EL PATRÒN 

  # El patrón es:
  # nuevo = a + b
  # Despues movemos los valores 
  # a = b
  # b = nuevo
  # y repetimos esto N veces 
  
  
# 4) ESCRIBIR EL CODIGO 
    
    
n = int(input("¿Cuántos? "))
a, b = 0, 1                         

for _ in range(n):                  
    print(a, end=" ")
    a, b = b, a + b               

print()                             













    
    
    
    
    

  



























































