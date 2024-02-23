#Se proporciona una lista de listas
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]
#Usaremos el metodo insert donde primero colocaremos i=indice de donde queremos insertar el elemento nuevo a la lista, y luego el contenido
recordatorios.insert(1,('2021-01-02',"06:00","Empezar el Año"))
#Para cambiar un elemento en especifico, colocaremos el indice de donde se encuentra el elemento en la lista, y luego el indice del dato que queremos cambiar 
recordatorios[3][0] = '2021-07-16'
#Usaremos el metodo remove para eliminar un elemento especifico de la lista 
recordatorios.remove(['2021-05-01', '15:00', 'No trabajar'])
#Usaremos insert para colocarlo en una posicion especifica
recordatorios.insert(4,('2021-12-24',"22:00","Cena de Navidad"))
#usaremos en este caso el metodo append ya que le corresponde el ultimo lugar en la lista de listas
recordatorios.append(['2021-12-31',"22:00","Cena de Año Nuevo"])
# Outputpython recordatorios.py 
print(recordatorios)
