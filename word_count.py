#En estas lineas de crearemos una var que contenga la ruta de donde se encuentra el archivo txt, para luego importarno en la linea 3 y 4 (texto seria la var que contenga el archivo txt)
ruta_archivo = "lorem_ipsum.txt"
with open(ruta_archivo, "r") as file:
    texto = file.read()
#Esta variable separa los caracteres distintos y los almacena 
caracteres_distintos = set(texto)
#Esta variable contara los caracteres distintos almacenados en la var caracteres_distintos
num_caracteres_distintos = len(caracteres_distintos)
#usaremos el metodo split que divide la cadena por los espacios en blanco que hay, generando una lista de las "palabras"
palabras = texto.split()
#Usaremos ahora el metodo set para almacenar los elementos unicos de esa lista anterior
palabras_distintas = set(palabras)
#Por ultimo utilizaremos len para contar cuantas palabras distintas hay en el texto
num_palabras_distintas = len(palabras_distintas)


print(f"El número de caracteres distintos es: {num_caracteres_distintos}")
print(f"El número de palabras distintas es: {num_palabras_distintas}")
#Me da como resultado 241 palabras distintas ya que los puntos en la dos palabras los considera parte de esas palabras 