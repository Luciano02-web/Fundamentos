print("----------")
print("  Vuelos  ")
print("----------")
#1. Carga de datos en una lista..
def leer_pasajes():
	lista = []
	destino = input('Ingrese destino: ').capitalize()
	while destino != 'Fin':
		origen = input('Ingrese origen: ').capitalize()
		fecha = input('Ingrese la fecha: ').capitalize()
		valor = int(input('Ingrese el valor$: '))
		nombre = input('Ingrese su nombre: ').capitalize()
		dato = [destino, origen, fecha, valor, nombre]
		lista.append(dato)
		destino = input('Ingrese destino o "Fin": ').capitalize()
	return lista
 
#2. Incluir funciones que realicen una tarea.
#-Imprime los pasajeros con destino a lo que desee el usuario.
def destinos_pasajeros(lista, destino_p):
	pasajeros=[]
	for d in lista:
		if d[0] == destino_p:
			pasajeros.append(d[4])
	print('Pasajeros con destino a '+destino_p+': '+str(pasajeros))

#3. Incluir consultas que retornen valores.
#-Retorna la cantidad de pasajeros con destino a lo que el usuario desee.
def cantidad(lista, des):
	cant=0
	resultado=0
	for c in lista:
		if c[0] == des:
			cant=cant+1
		else:
			resultado=resultado+1
	return(str(cant)+' pasajeros tienen destino a '+des)

#4. Incluir consultas que retornen listas.
#-Retorna la lista cuyo origen desee el usuario.
def origen_lista(lista, origen_l):
	lista_origen=[]
	for d in lista:
		if d[1] == origen_l:
			lista_origen.append(d)
	return(lista_origen)

#5. Incluir consultas que retornen un valor booleano.
#-Retorna si el destino que desea el usuario se encuentra en la lista o no.
def buscador_destinos(lista,buscar):
	for b in lista:
		if b[0]==buscar:
			return (buscar +' se encuentra en la lista')
		else:
			return (buscar +' no se encuentra en la lista')

#6. Retornar el elemento que sea máximo o mínimo para algún valor.
#-Retorna el destino con el valor maximo de la lista.
def maxi(lista):
	maximo=0
	for m in lista:
		if m[3]>maximo:
			maximo=m[3]
			res1=m[0]
	return res1
#-Retorna el valor maximo de la lista.
def maxi2(lista):
	maximo=0
	for m in lista:
		if m[3]>maximo:
			maximo=m[3]
	return maximo

#6. bis
#-Retorna el destino con el valor minimo de la lista.
def mini(lista):
	minimo=1000000000
	for mi in lista:
		if mi[3] < minimo:
			minimo = mi[3]
			res2 = mi[0]
	return res2
#-Retorna el valor minimo de la lista.
def mini2(lista):
	minimo=1000000000
	for mi in lista:
		if mi[3] < minimo:
			minimo = mi[3]
	return minimo

#7. Retornar el promedio de algún valor.
#-Retorna el promedio de los valores del destino que se desee.
def promedio(lista,dest):
	cantidad = 0
	suma = 0
	for p in lista:
		if p[0] == dest:
			suma = suma + p[3]
			cantidad = cantidad + 1
	if cantidad == 0:
		promedio = 0
	else:
		promedio = suma / cantidad
	return promedio

#Retorna la lista con el nombre mas largo.
def nombre_mas_largo(lista):
	maximo = 0
	for pasajero in lista:
		if(maximo < len(pasajero[4])):
			maximo = len(pasajero[4])
			resultado = pasajero
	return resultado

#Imprime la cantidad de nombres que empiezan con vocal y sus respectivas listas.
def comienza_con_vocal(lista):
	vocales='A','E','I','O','U'
	contar=0
	resultado=0
	res=[]
	for nombre in lista:
		if nombre[4][0] in vocales:
			contar=contar+1
			res.append(nombre)
		else:
			resultado=resultado+1
	print('La cantidad de nombres que comienzan con vocal son '+str(contar)+' y sus datos son '+str(res))

#Retorna el promedio total de todos los valores.
def promedio_total(lista):
	suma=0
	cantidad=0
	for val in lista:
		if val[3] > -10000000:
			suma = suma + val[3]
			cantidad = cantidad + 1
			promedio = suma/cantidad
	return promedio

#Menu
pasajes=leer_pasajes()
menu="""Opciones:\n1: Permite mostrar todos los pasajes vendidos(imprime todas las listas).
\n2: Ver la cantidad de palabras ingresadas.
\n3: Ver el/los pasajero/s del destino que se desee.
\n4: Ver la cantidad de veces que se repite algun destino en la lista.
\n5: Ver la/s lista/s del origen que se desee.
\n6: Ver si el destino que se ingresa está presente en la lista o no.
\n7: Ver el destino con el valor más elevado y su respectivo valor.
\n8: Ver el destino con el valor más elevado y su respectivo valor.
\n9: Ver el promedio de los valores del destino que se desee.
\n10: Ver la lista con el nombre mas largo.
\n11: Ver la cantidad de nombres que comienzan con vocal y sus datos.
\n12: Ver el promedio total de todos los valores ingresados."""
print(menu)
opcion=int(input('Ingrese una opcion: '))
while opcion != 0:
	if opcion == 1:#permite mostrar todos los pasajes vendidos(imprime todas las listas).
		print(pasajes)
		print('-------------------')
	elif opcion == 2:#permite ver la cantidad de palabras ingresadas.
		print('La cantidad de destinos ingresados son: '+str(len(pasajes)))
		print('-------------------')
	elif opcion == 3:#permite ver el/los pasajero/s del destino que se desee.
		destino_p = input('Ingrese destino del cual desee saber sus pasajeros: ').capitalize()
		destinos_pasajeros(pasajes, destino_p)
		print('-------------------')
	elif opcion == 4:#permite ver la cantidad de veces que se repite algun destino en la lista.
		des=input('Ingrese destino que desee saber la cantidad de veces que esta presente en la lista: ').capitalize()
		cantidad_des = cantidad(pasajes, des)
		print(cantidad_des)
		print('-------------------')
	elif opcion == 5:#permite ver la/s lista/s del origen que se desee.
		origen_l = input('Ingrese origen del cual desee saber sus datos: ').capitalize()
		con_origen = origen_lista(pasajes, origen_l)
		print('Los datos de los pasajeros con origen a '+origen_l+' son '+str(con_origen))
		print('-------------------')
	elif opcion == 6:#permite ver si el destino que se ingresa está presente en la lista o no.
		buscar = input('Ingrese destino que desee buscar: ').capitalize()
		buscador = buscador_destinos(pasajes,buscar)
		print (buscador)
		print('-------------------')
	elif opcion == 7:#permite ver el destino con el valor más elevado y su respectivo valor.
		destino_max = maxi(pasajes)
		destino_max2 = maxi2(pasajes)
		print('El destino con el valor más elevado es el destino a '+destino_max+' con un valor de '+str(destino_max2))
		print('-------------------')
	elif opcion == 8:#permite ver el destino con el valor más bajo y su respectivo valor.
		destino_mini = mini(pasajes)
		destino_mini2 = mini2(pasajes)
		print('El destino con el valor más bajo es el destino a '+destino_mini+' con un valor de '+str(destino_mini2))
		print('-------------------')
	elif opcion == 9:#permite ver el promedio de los valores del destino que se desee.
		dest = input('Ingrese destino del cual desee saber el promedio de sus valores: ').capitalize()
		prom_dest_val = promedio(pasajes,dest)
		print('El promedio de los valores con destino a '+ dest +' es: ' + str(prom_dest_val))
		print('-------------------')
	elif opcion == 10:#permite ver la lista con el nombre mas largo.
		mas_largo=nombre_mas_largo(pasajes)
		print('La lista con el nombre más largo es esta: '+str(mas_largo))
		print('-------------------')
	elif opcion == 11:#permite ver la cantidad de nombres que comienzan con vocal y sus datos.
		comienza_con_vocal(pasajes)
		print('-------------------')
	elif opcion == 12:#permite ver el promedio total de todos los valores ingresados.
		promedio_total_valores=promedio_total(pasajes)
		print('El promedio total de todos los valores ingresados es de: '+str(promedio_total_valores))
		print('-------------------')
	else:
		print('Opcion invalida')
		print(menu)
	opcion=int(input('Ingrese una opcion o 0 para finalizar: '))
print('---------------------------')
print('Gracias por usar el sistema')
print('---------------------------')


