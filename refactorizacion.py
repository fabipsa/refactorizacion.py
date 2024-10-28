def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            if point < 1 or point > 5:
                print('Por favor, introduzca un valor entre 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                try:
                    with open("data.txt", 'a') as file_pc:
                        file_pc.write(f'{post}\n')
                except Exception as e:
                    print(f'Error al escribir en el archivo: {e}')
                break
        else:
            print('Por favor, introduzca la puntuación en números')


def comprobar_resultados():
    try:
        with open("data.txt", "r") as read_file:
            contenido = read_file.read()
            if contenido:
                print('Resultados hasta la fecha:')
                print(contenido)
            else:
                print('No hay resultados registrados hasta ahora.')
    except FileNotFoundError:
        print('El archivo no existe. No se pueden mostrar resultados.')


def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprobar los resultados obtenidos hasta ahora')
        print('3: Finalizar')
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                confirmacion = input('¿Está seguro de que desea finalizar? (s/n): ')
                if confirmacion.lower() == 's':
                    print('Finalizando')
                    break
            else:
                print('Por favor, introduzca un número del 1 al 3')
        else:
            print('Por favor, introduzca un número del 1 al 3')


if __name__ == "__main__":
    main()
