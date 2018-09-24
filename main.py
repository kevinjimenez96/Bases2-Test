import redis
import sys
from colorama import Fore
from colorama import Style

r = redis.Redis(host='localhost', port=6379, db=0)
while True:
    print(f'{Style.BRIGHT}¡Bienvenido al sistema de información de estudiantes!{Style.RESET_ALL}')
    print(f'1) Agregar un nuevo estudiante')
    print(f'2) Consultar la información de un estudiante')
    print(f'3) Eliminar un estudiante')
    print(f'4) Agregar un curso')
    print(f'5) Salir')
    seleccion = int(input(f'{Fore.LIGHTYELLOW_EX}Por favor, ingrese el numero correspondiente a la tarea que desea realizar: {Style.RESET_ALL}'))
    if seleccion == 1:
        carnet = input(f'{Fore.LIGHTYELLOW_EX}Ingrese el número de carnet del estudiante:{Style.RESET_ALL}')
        nombre = input(f'{Fore.LIGHTYELLOW_EX}Ingrese el nombre del estudiante:{Style.RESET_ALL}')
        carrera = input(f'{Fore.LIGHTYELLOW_EX}Ingrese la carrera a la que pertenece el estudiante:{Style.RESET_ALL}')
        ponderado = float(input(f'{Fore.LIGHTYELLOW_EX}Ingrese el ponderado del estudiante:{Style.RESET_ALL}'))
        #cursos = [x for x in input(f'{Fore.LIGHTYELLOW_EX}Ingrese los cursos a los que el estudiante pertenece:{Style.RESET_ALL}').split()]
        r.set(f'estudiante:{carnet}:nombre', nombre)
        r.set(f'estudiante:{carnet}:carrera', carrera)
        r.set(f'estudiante:{carnet}:ponderado', ponderado)
    elif seleccion == 2:
        carnet = input(f'{Fore.LIGHTYELLOW_EX}Ingrese el número de carnet del estudiante:')
        if r.exists(f'estudiante:{carnet}:nombre'):
            print(f'{Fore.LIGHTGREEN_EX}Nombre:      {Style.RESET_ALL}' + str(r.get(f'estudiante:{carnet}:nombre').decode("utf-8")))
            print(f'{Fore.LIGHTGREEN_EX}Carrera:     {Style.RESET_ALL}' + str(r.get(f'estudiante:{carnet}:carrera').decode("utf-8")))
            print(f'{Fore.LIGHTGREEN_EX}Ponderado:   {Style.RESET_ALL}' + str(float(r.get(f'estudiante:{carnet}:ponderado'))))
        else:
            print(f'{Fore.LIGHTRED_EX}Ingrese que el carnet sea valido y/o haya sido agregado al sistema anteriormente.{Style.RESET_ALL}')
    elif seleccion == 3:
        if input(f'{Fore.RED}Esta operación no es reversible, ¿Desea continuar? {Style.RESET_ALL}S/n: ') == 'S':
            carnet = input(f'{Fore.RED}Ingrese el número de carnet del estudiante:{Style.RESET_ALL}')
            pattern = r'estudiante:{0}:*'.format(carnet)
            c, estudiante_keys = r.scan(0, pattern)
            for x in estudiante_keys:
                r.delete(x)
            print(f'{Fore.LIGHTGREEN_EX}¡Se ha eliminado al estudiante con exito!{Style.RESET_ALL}')
    elif seleccion == 4:
        siglas = input(f'{Fore.LIGHTYELLOW_EX}Ingrese las siglas del curso y su respectivo semestre (curso-semestre):{Style.RESET_ALL}')
        nombre = input(f'{Fore.LIGHTYELLOW_EX}Ingrese el nombre del curso:{Style.RESET_ALL}')
        profesor = input(f'{Fore.LIGHTYELLOW_EX}Ingrese la ingrese el profesor del curso:{Style.RESET_ALL}')
        cupo = float(input(f'{Fore.LIGHTYELLOW_EX}Ingrese el cupo del curso:{Style.RESET_ALL}'))
        r.set(f'curso:{siglas}:nombre', nombre)
        r.set(f'curso:{siglas}:carrera', profesor)
        r.set(f'curso:{siglas}:ponderado', cupo)
    elif seleccion == 5:
        sys.exit()
    else:
        print('Inserte un número valido por favor.')
    input('Oprima enter para continuar:')