import random
def guardar_reserva(lista_de_reservas):
    print("Ha seleccionado la opcion 1")
    fecha_ingreso=input("Seleccione la Fecha de ingreso: ")
    hora_paseo=input("Seleccione la hora del paseo: ")
    lugar_inicio=input("Seleccione el lugar de inicio: ")
    lugar_fin=input("Seleccione el final del recorrido: ")
    nombre_persona_reserva=input("Ingrese el nombre de la persona que reserva")
    cantidad_de_mascotas=int(input("Seleccione la cantidad de mascotas a pasear: "))
    if cantidad_de_mascotas > 5:
            print("La cantidad de mascotas debe ser menor a 5")
            cantidad_de_mascotas=int(input("Seleccione la cantidad de mascotas a pasear: "))
    elif cantidad_de_mascotas <= 0:
        print("Debe haber almenos una mascota ingresada")
        cantidad_de_mascotas=int(input("Seleccione la cantidad de mascotas a pasear: "))
    lista_de_reservas.append([fecha_ingreso,hora_paseo,lugar_inicio,lugar_fin,cantidad_de_mascotas,nombre_persona_reserva])
    return lista_de_reservas





def buscar_reserva(lista_de_reservas):
    print("Seleccionó la opción 2")
    reserva_buscada=int(input("Ingrese numero de la reserva"))
    largo_lista=len(lista_de_reservas)
    posicion_reserva_en_la_lista=-1
    mensaje="La habitación está vacía" 
    for fila in range(largo_lista):
        print("Impreso automaticamente",lista_de_reservas[fila])
        reserva_encontrada=lista_de_reservas[fila]
        numero_reserva_encontrada=reserva_encontrada[0]

def mostrar_reserva(lista_de_reservas):
    print("Seleccionó la opción 3")
    print("----------Boleta----------")
    print("")
    print("")
    print("")
    print("")
    print("el precio en total fueron", precio)
    precio = random.randint(3500,12900)


#Los montos deben ser previamente ingresados con valores aleatorios entre $3500 y $12.900. 
# Al imprimir la boleta, debe mostrar la fecha del viaje, la cantidad de mascotas paseadas y el precio del paseo.