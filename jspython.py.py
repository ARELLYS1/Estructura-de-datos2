# EJERCIO_1 SALUDO PERSONALIZADO 
# LEER EL NOMBRE DEL USUARIO Y SALUDARLO POR SU NOMBRE

# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   #Nombre (input)
   
   # 2 proceso - que hago con eso 
   # concatenar «Hola,» con el nombre
   
   # 3 Salida - Què debo mostrar 
   # el saludo completo 
   
# 2) BOSQUEJO A MANO 
   # nombre = "Ana"

   # Salida:  Hola, Ana. Bienvenida al curso.
   
# 3) DESCUBRIR EL PATRÒN 
  # Hay un solo dato de entrada (nombre) y no hay que hacer 
  # cuentas, solo formar un mensaje. Este es el patrón más simple: leer → mostrar.

  # Como input() ya devuelve str, no necesitamos convertir nada.

#  4) ESCRIBIR EL CÒDIGO

nombre = input ("INGRESE SU NOMBRE: ")
edad = int(input("cuantos años tienes: "))
print(f"Hola, {nombre}. Bienvenida al curso. tengo {edad} años") 


# EJERCICIO_2 PROMEDIO DE TRES NOTA 
# LEER TRES NOTAS DE UN ESTUDIANTE Y MOSTRAR SU PROMEDIO 

 # 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # n1, n2, n3 (input)
   
   # 2 proceso - que hago con eso 
   # sumar las tres y dividir para tres 
   
   # 3 Salida - Què debo mostrar 
   # el promedio 
   
# 2) BOSQUEJO A MANO 
   # n1 = 8, n2 = 6, n3 = 10

   # paso 1: sumo    8 + 6 + 10 = 24
   # paso 2: divido  24 / 3     = 8.0
   # paso 3: muestro "Promedio: 8.0"
   
# 3) DESCUBRIR EL PATRÒN 
    # El proceso tiene dos pasos: primero sumar, despues dividir. los parèntesis son obligatorios: sin ellos solo divide n3 para 3.
    # El 3 no se lee: es un valor fijo del problema (siempre son tres notas). Solo se lee lo que el usuario decide.
    # En python/ siempre da float (8.0, no 8). perfecto: el promedio casi siempre tiene decimales.
    
#4) ESCRIBIR EL CÒDIGO 

n1= float(input("ingrese la primera nota: "))
n2= float(input("ingrese la segunda nota: "))
n3= float(input("ingrese la tercera nota: "))

promedio= (n1+n2+n3)/3
if promedio >=7:
    print(f"el promedio es: {promedio} aprueba")
elif promedio < 7:
     print (f"el promedio es: {promedio} reprueba")
    
      
# EJERCICIO_3 ÀREA Y PERIMETRO DE UN RECTANGULO 
# LEER LA BASE Y LA ALTURA DE UN RECTANGULO Y MOSTRAR SU ÀREA Y SU PERIMETRO. RECUERDA: ÀREA= BASE X ALTURA, PERÌMETRO= 2 X(BASE+ALTURA)

# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # base, altura (input)
   
   # 2 proceso - que hago con eso 
   # aplicar las dos fòrmulas
   
   # 3 Salida - Què debo mostrar 
   # el àrea y el prerimetro 
   
 #2) BOSQUEJO A MANO 
   # base = 5, altura = 3

   #área = 5 × 3 = 15
   # perímetro = 2 × (5 + 3) = 16

#3) DESCUBRIR EL PATRÒN 
   # Dos entrada y dos salidas, independientes: cada fòrmula usa base y altura poro separado. no hay bucles ni decisiones.
   # como pueden venir decimales ( una base de 5.5cm es vàlida ), usamos float.

#4) ESCRIBIR EL CÒDIGO 

import math

base= float(input("ingrese la base: "))
altura= float(input("ingrese la altura: "))
radio = float(input("ingrese el radio: "))


area= base * altura
perimetro= 2 * (base+altura)



print(f"el area es: {area} y el perimetro es: {perimetro}")        
print(f"El área del círculo es: {math.pi * radio**2} y el perímetro es: {2 * math.pi * radio}")

# EJERCICIO_4 CONVERTIR GRADOS CELSIUS A FAHRENHEIT 
#Pide una temperatura en grados celsius y muèstrala en fahrenheit. formula: F=c x 9/5 +32.

# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # grados celsius (input)
   
   # 2 proceso - que hago con eso 
   # aplicar formula
   
   # 3 Salida - Què debo mostrar 
   # grados en fahrenheit 
   
   #2) BOSQUEJO A MANO 
   
   # celsius = 25
   # fahrenheit = 25 x 9/5 + 32 = 77.0
   
#3) DESCUBRIR EL PATRÒN 





# 4) ESCRIBIR CÒDIGO   

celsius = float(input("ingrese la temperatura en grados celsius: "))

fahrenheit = celsius * 9/5 +32

print(f"la temperatura en fahrenheit es: {fahrenheit}")


# EJERCICIO_5 SEGUNDOS A HORAS, MINUTOS Y SEGUNDOS 
# Pide un total de segundos y muestralos como hh:mm:ss. Ej:3725 segundos 1:02:05.

# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # segundos (input)
   
   # 2 proceso - què hago con eso 
   # dividir los segundos en horas, minutos y segundos usando división entera (//) y módulo (%)

   # 3 Salida - Què debo mostrar 
   # el tiempo en formato horas:minutos:segundos (con ceros a la izquierda en min y seg)

# 2) BOSQUEJO A MANO 
   #seg = 3725
   #horas    = 3725 // 3600 = 1
   #resto    = 3725 % 3600  = 125
   #minutos  = 125 // 60    = 2
   #segundos = 125 % 60     = 5
   #resultado: 1:02:05
   
   #3) DESCUBRIR EL PATRÒN 
   # una sola entrada, pero se van "desglosando" partes sucesivas: primero se extraen 
   # las horas, y lo que sobra (resto) se vuelve a desglosar para sacar minutos, 
   # y lo que sobra de eso son los segundos.
   # No hay bucles ni decisiones, solo operaciones de // y % encadenadas.
   # Como los segundos totales son una cantidad entera (no tiene sentido decir 
   # "3725.5 segundos" en este contexto), usamos int.

# 4) ESCRIBIR EL CÒDIGO 

total = int(input("Segundos totales: "))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas}:{minutos:02d}:{segundos:02d}")


# EJERCICIO_6 INTERCAMBIAR DOS VARIABLES 
# Lee dos números y muéstralos intercambiados. Python permite hacerlo en una sola línea, muy diferente a JS.
  
 # 1) ENTENDER EL PROBLEMA 
   
   # 1 ENTRADA - QUÈ ME DAN 
   # a,b (input)
   
   # 2 proceso - què hago con eso 
   # Intercambiar los valores: a pasa a valer lo que tenía b, y b pasa a valer lo que tenía a

   # 3 Salida - Què debo mostrar 
   # Los valores intercambiados 

# 2) BOSQUEJO A MANO 

   # a= 8, b=3
   
   # intercambio: a=3, b=8 
   
# 3) DESCUBRIR EL PATRÒN 

   # Una sola entrada, dos variables, y un solo proceso: intercambiar.
   # no hay bucles ni decisiones, solo operaciones de asignaciòn.
   
# 4) ESCRIBIR EL CÒDIGO 

a = int(input("a: "))
b = int(input("b: "))

# Intercambio pythónico (una sola línea)
a, b = b, a

print(f"a = {a}, b = {b}")


# EJERCICIO_7 CALCULAR EL IVA (15% ECUADOR)
# Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.

# 1) ENTENDER EL PROBLEMA 
   # 1 ENTRADA - QUÈ ME DAN 
   # precio (input)
   
   # 2 proceso - què hago con eso 
   # aplicar la fòrmula: iva = precio *0.15, total = precio + iva 

   # 3 Salida - Què debo mostrar 
   # mostrar el iva 
   
# 2) BOSQUEJO A MANO  
precio= 200

iva = 0.15
total = precio + (precio * iva) 

# 3) DESCUBRIR EL PATRÒN 

# una sola entrada, dos salidas, y un solo proceso: 
# calcular el iva y el total.

# 4) ESCRIBIR EL CÒDIGO 

precio = float(input("Precio sin IVA: $"))
iva = precio * 0.15
total = precio + iva

print(f"IVA:   ${iva:.2f}")
print(f"Total: ${total:.2f}") 