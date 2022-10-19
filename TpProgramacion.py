#Listado de Artistas/Canciones
from ast import Break
import string


Lista1 = [["Linkin Park", "Numb"],["Linkin Park", "In The End"],["Linkin Park", "Somewhere I belong"],["Quien Sabe" , "Mi Bebito Fiu Fiu"],["Pulcino Pio", "Pollito Pio"]]
#Lista de Letras
Lista2 = [["I'm tired of being what you want me to be \n Feeling so faithless, lost under the surface \n I don't know what you're expecting of me \n Put under the pressure of walking in your shoes \n Caught in the undertow, just caught in the undertow \n Every step that I take is another mistake to you \n Caught in the undertow, just caught in the undertow"],["It starts with \n One thing I don't know why \n It doesn't even matter how hard you try \n Keep that in mind \n  I designed this rhyme to explain in due time \n All I know \n Time is a valuable thing \n  Watch it fly by as the pendulum swings \n  Watch it count down to the end of the day \n The clock ticks life away"],["When this began \n I had nothing to say \n And I get lost in the nothingness inside of me \n (I was confused) \n  And I let it all out to find \n That I'm not the only person with these things in mind \n (Inside of me) \n But all that they can see the words revealed \n Is the only real thing that I've got left to feel \n (Nothing to lose) \n Just stuck, hollow and alone \n And the fault is my own, and the fault is my own"],["Caramelo de chocolate \n Empápame así \n Como un pionono de vitrina \n Enróllame así \n Con azúcar en polvo endúlzame \n Y es que tú eres mi rey \n Eres mi bebé \n Mi bebito Fiu Fiu"],["En la radio, hay un pollito \n En la radio, hay un pollito \n  El pollito pío, el pollito pío \n El pollito pío, el pollito pío \n El pollito pío, el pollito pío \n \n En la radio, hay una gallina \n En la radio, hay una gallina \n Y la gallina coo, y el pollito pío \n Y el pollito pío, y el pollito pío \n Y el pollito pío, y el pollito pío \n \n En la radio, hay también un gallo \n En la radio, hay también un gallo \n  Y el gallo corococo, y la gallina coo \n Y el pollito pío, el pollito pío \n El pollito pío, el pollito pío"]]

#Funcion para elecciones

def elecciones():
    while True:
        try: 
            eleccion = int(input("que desea hacer? \n 1- Ver la lista de canciones? \n 2- Ver la letra de las canciones? \n 3- Agregar una cancion: \n 4- Eliminar una cancion?\n 5- Volver a hacer las preguntas \n 6-Buscar por nombre \n 7-Terminar \n : "))
        
            if eleccion == 1:
             vercanciones()
            if eleccion == 2:
              seleccionarletra()
            if eleccion == 3:
               agregarcancion()
            if eleccion == 4:
              borrarcancion()
            if eleccion == 5:
               elecciones()
            if eleccion ==6:
              buscarnombre()  
            else:   
              if eleccion == 7:
               print("Adios ಠᴗಠ")
               Break
                  
        except:
          print("Error en la eleccion ಠ_ಠ \nelegir una opcion Numerica:")
          eleccion = int(input("1-intentar de nuevo? \n2- Cerrar programa \n:"))
          if eleccion == 1:
            elecciones()
          if eleccion == 2:
            print("El programa Termino  ͡ಠᴗಠ ")
                 
#Funcion para ver la lista de las canciones

def vercanciones():
    print("Estas son las canciones Disponibles \n")
    for i in Lista1:
        print(Lista1.index(i)+1 , "-" , i[0] + ", " + i[1] )
    elecciones()

#Funcion para seleccionar la letra de la cancion

def seleccionarletra():
    letra = int(input("que letra queres leer?: "))
    print(Lista2[letra-1])

#Funcion para agregar una cancion

def agregarcancion():
    eleccion = input("Agregar nombre de la banda y cancion: ")
    eleccion2 = ingresarletra()
    Lista1.append(eleccion)
    print("Cancion Agregada")
    elecciones()
    
#Funcion para borrar una cancion
    
def borrarcancion():
    eleccion = int(input("¿Que canción deseas eliminar?: "))
    del Lista1[eleccion - 1]
    print("\nCanción eliminada\n")
    elecciones()

#buscar por Nombre

def buscarnombre():
    eleccion = (input("Cual queres buscar?: "))
    for i in Lista1:
      if eleccion in i:
        print("es la opcion numero:", i)
      else:
        print("no se encontro")

#Funcion para ingresar letra

def ingresarletra():
    eleccion = ""
    print("Ingrese la letra de la canción. Para nuevo renglón enter y la letra f para terminar")
    letra = input()
    while eleccion != "f" and eleccion != "F":
        eleccion = eleccion + "\n" + letra
        eleccion = input("Ingrese nueva línea, f para terminar\n")
        Lista2.append(letra)
    return eleccion

elecciones()

