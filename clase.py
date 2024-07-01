"""
función para determinar la edad de una persona 
por el año de nacimiento
"""
import datetime

def anio_nacimiento():
  anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
  current_year = datetime.datetime.now().year
  age = current_year - anio_nacimiento

  return print(f"Tu edad es: {age}")
 

anio_nacimiento()