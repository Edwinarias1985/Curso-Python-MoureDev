### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)
print(len("Este es el valor de:"), my_bool_variable, "teóricos facultativos", my_string_variable)

print(type(print("Mi cadena de texto"))) # Tipo dato 'NoneType' (Ningun tipo)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. Cuidado con abusar de esta sintaxis

name, surname, alias, age = "Edwin", "Arias", "Megalomania", 39
print("Me llamo:", name, surname, "Mi edad es", "Y mi alias es:", alias)

#Inpust's
name = input('¿Cuál es tu nombre? ')
age = input("¿Cuántos años tienes? ")
deporte = input('¿Cuál es tu deporte favorito? ')

print(name)
print(age)
print(deporte)
print("Tu nombre es:", name, "Tienes", age, "años", "Deporte favorito", deporte)

# Cambiamos su tipo

name = 20 # A esta variable name se le puede cambiar el tipo dato a integer (entero)
age = "Edwin" # Igual pasa, se puede cambier tipo de dato a string

#¿Forzamos el cierre?
direccion: str = "av circunbalar"
direccion = 85
direccion: float = 20.2
print(type(direccion))