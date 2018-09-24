import redis
import sys
import re

r = redis.Redis(host='localhost', port=6379, db=0)
while True:
    print('¡Bienvenido al sistema de información de estudiantes!')
    print('1) Agregar un nuevo estudiante')
    print('2) Consultar la información de un estudiante')
    print('3) Eliminar un estudiante')
    print('4) Salir')
    seleccion = int(input('Por favor, ingrese el numero correspondiente a la tarea que desea realizar: '))
    if seleccion == 1:
        carnet = input('Ingrese el número de carnet del estudiante:')
        nombre = input('Ingrese el nombre del estudiante:')
        carrera = input('Ingrese la carrera a la que pertenece el estudiante:')
        ponderado = float(input('Ingrese el ponderado del estudiante:'))
        r.set(f'estudiante:{carnet}:nombre', nombre)
        r.set(f'estudiante:{carnet}:carrera', carrera)
        r.set(f'estudiante:{carnet}:ponderado', ponderado)
    elif seleccion == 2:
        carnet = input('Ingrese el número de carnet del estudiante:')
        if r.exists(carnet):
            print(str(r.get(f'estudiante:{carnet}:nombre').decode("utf-8") ))
            print(str(r.get(f'estudiante:{carnet}:carrera').decode("utf-8") ))
            print(float(r.get(f'estudiante:{carnet}:ponderado')))
        else:
            print('\033[93mIngrese que el carnet sea valido y/o haya sido agregado al sistema anteriormente.\033[0m')
        input('Oprima enter para continuar:')
    elif seleccion == 3:
        carnet = input('Ingrese el número de carnet del estudiante:')
        pattern = r'estudiante:{0}:*'.format(carnet)
        c, estudiante_keys = r.scan(0, pattern)
        for x in estudiante_keys:
            r.delete(x)
    elif seleccion == 4:
        sys.exit()
    else:
        print('Inserte un número valido por favor.')