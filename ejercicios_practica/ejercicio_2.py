# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print(f"{texto_1} es mayor alfabeticamente que {texto_2}")
elif texto_1 < texto_2:
       print(f"{texto_1} es menor alfabeticamente que {texto_2}")
else:
      print(f"{texto_1} es igual alfabeticamente que {texto_2}")      


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):
    print(f"{texto_1} tiene mayor cantidad de letras que {texto_2}")
elif len(texto_1) < len(texto_2):
    print(f"{texto_1} tiene menor cantidad de letras que {texto_2}")
else:
    print(f"{texto_1} tiene igual cantidad de letras que {texto_2}")    

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1 [:-1] > texto_2 [:-1]:
    print(f"la primer letra de {texto_1} es mayor a la primer letra de {texto_2}")
elif texto_1 [:-1] < texto_2 [:-1]:
    print(f"la primer letra de {texto_1} es menor a la primer letra de {texto_2}")
else:
    print(f"la primer letra de {texto_1} es igual a la primer letra de {texto_2}")

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print(f"{copia_texto_1} es igual a {texto_1}") 
else:
    print(f"{copia_texto_1} no es igual a {texto_1}")


# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 != texto_2:
    print(f"{copia_texto_1} es distinto a {texto_2}") 
else:
    print(f"{copia_texto_1} no es distinto a {texto_2}")
