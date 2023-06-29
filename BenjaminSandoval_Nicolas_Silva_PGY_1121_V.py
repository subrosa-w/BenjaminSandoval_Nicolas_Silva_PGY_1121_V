from funciones import*
import random
menu=True
opcion_seleccionada=0
numero_de_reserva=1000
lista_de_reservas=[
["6 de mayo","5 de la tarde","plaza de armas","guillermo gallardo","4","Franco soto", 997],
["21 de agosto","8 de la mañana","valle volcanes","universidad san sebastian","2","aaaa", 998],
["15 de junio","2 de la tarde","colegio pumahue","jardin oriente","6","Nicolas Silva", 999],
]
numero_de_reserva=1000
#Fecha, Hora del paseo, Lugar de inicio, lugar de fin
# cantidad de mascotas a pasear, nombre de la persona que reserva, número de la reserva 
while menu == True:
    print("-------Menu Empresa Te Paseo-------\n")
    print("1.- Grabar: \n")
    print("2.- Buscar: \n")
    print("3.- Imprimir Boleta: \n")
    print("4.- Salir\n")
    opcion_seleccionada=int(input("Seleccione una opcion: "))

#/////////////////////////////////////////////////////////////////////////////////////////////////////////
    if opcion_seleccionada == 1:
        reserva_modificada=guardar_reserva(lista_de_reservas)

        lista_de_reservas=reserva_modificada
        print("Reserva guardada con éxito")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////
    if opcion_seleccionada == 2:
        print("Ha seleccionado la opcion 2")
        buscar_reserva(lista_de_reservas)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////
    if opcion_seleccionada == 3:
        print("Ha seleccionado la opcion 3")
#Los montos deben ser previamente ingresados con valores aleatorios entre $3500 y $12.900. 
# Al imprimir la boleta, debe mostrar la fecha del viaje, la cantidad de mascotas paseadas y el precio del paseo.
#/////////////////////////////////////////////////////////////////////////////////////////////////////////
    if opcion_seleccionada == 4:
        print("Ha seleccionado la opcion 4")
        print("Saliendo del programa...")
        print("programa hecho por Benjamin Sandoval y Nicolas Silva\n")
        print("Version 1.1")
        menu=False    