import sys 
#aca indicaremos con el float que los argumentos que se ingresaran son de tipo numeros con decimales
sol_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
peso_chileno = int(sys.argv[4])
#aca haremos una variable para cada conversion de divisa 
con_chi_pe = peso_chileno * sol_peruano
con_chi_arg = peso_chileno * peso_argentino
con_chi_dolar = peso_chileno * dolar_americano
#Por ultimo aca imprimeremos el resultado llamando a lso resultados de nuestras var
print(f"Los {peso_chileno} pesos equivalen a : \n {con_chi_pe} Soles \n {con_chi_arg} Pesos ARgentinos \n {con_chi_dolar} Dólares")

