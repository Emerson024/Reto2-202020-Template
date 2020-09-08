"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

file1= 'Data/theMoviesdb/MoviesCastingRaw-small.csv'
file2= 'Data/theMoviesdb/SmallMoviesDetailsCleaned.csv'




# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print('1- Iniciar listas')
    print("2- Cargar Datos")
    print("3- Mejores peliculas de un director")#requerimiento 1
    print("4- Crear ranking de peliculas")#requerimiento 2
    print("5- Conocer un director") #requerimiento 3
    print("6- Conocer un actor")#requerimiento 4
    print('7- Entender un genero')#requerimiento 5
    print("8- Ranking del Genero")#requerimiento 6
    print("0- Salir")


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                lst= controller.nueva_lista()
                lst2= controller.nueva_lista()

            elif int(inputs[0])==2: #opcion 2
                p1= controller.carga_de_datos(file1,lst,lst2,file2)[0]
                p2= controller.carga_de_datos(file1,lst,lst2,file2)[1]

            elif int(inputs[0])==3: #opcion 3
               pass   

            elif int(inputs[0])==4: #opcion 4
                pass

            elif int(inputs[0])==5: #opcion 5
                pass
        
            elif int(inputs[0])==6: #opcion 6
                pass
            elif int(inputs[0])==7: #opcion 7
                pass
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()
