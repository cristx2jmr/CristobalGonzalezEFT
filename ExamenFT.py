juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}

def leer_opcion():
        try:
            opt = int(input("Ingrese una opcion: "))
            return opt
        except ValueError:
            print("ingrese una opcion numerica")

def stock_plataforma(plaraforma):
    disponibles = 0
    for i in juegos:
        if plataforma == juegos[i][1]:
            disponibles += inventario[i][1]
    print(f"los juegos disponibles en esta plataforma son {disponibles}")


def busqueda_precio(p_min, p_max):
    for i in inventario:
        if inventario[i][0] > p_min and inventario[i][0] < p_max:
            print(f"el juego {juegos[i][0]} {i} esta en el rango de precio")
            if inventario[i][1] == 0:
                print(f"el {juegos[i][0]} no tiene stock disponible")


def buscar_codigo(codigo):
    for i in inventario:
        if i == codigo:
            print(i)
            return True
        else:
            print("no se encuentra este codigo")
            return False
        
def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo) == True:
        for i in inventario:
            if codigo == i:
                inventario[i][0] = nuevo_precio
                print("precio cambiado exitosamente")
                print(f"datos de los cambios: \ncodigo: {i}\nprecio: {nuevo_precio}")
                print(inventario)

def eliminar_juego(codigo):
    if buscar_codigo(codigo) == True:
        for i in inventario:
            if codigo == i:
                inventario.remove(i)
                juegos.remove(i)
    print(juegos)
    print(inventario)


opt = 0
while opt != 6:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Búsqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")
    print("=====================================")
    match leer_opcion():
        case 1:
            plataforma = input("ingrese plataforma que desea buscar: ")
            plataforma = plataforma.upper().strip()
            stock_plataforma(plataforma)
        case 2:
            try:
                p_min = int(input("ingrese monto min: "))
                p_max = int(input("ingrese precio maximo: "))
            except ValueError:
                print("debe ingresar valores enteros.")
            else:
                busqueda_precio(p_min, p_max)
        case 3:
            codigo = input("ingrese codigo: ").upper()
            nuevo_precio = int(input("ingrese nuevo valor: "))
            actualizar_precio(codigo, nuevo_precio)
        case 4:
            print("")
        case 5:
            codigo = input("ingrese codigo: ").upper()
            eliminar_juego(codigo)
        case 6:
            print("Saliendo...")
            break