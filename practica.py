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


def buscar_codigo(codigo):
    for i in inventario:
        if i == codigo:
            print(i)
            return True
        else:
            print("no se encuentra este codigo")
            return False


            
def eliminar_juego(codigo):
    if buscar_codigo(codigo) == True:
        for codigo in inventario:
            if codigo == inventario:
                inventario.remove(codigo)
                juegos.remove(codigo)
    print(juegos)
    print(inventario)

codigo = input("ingrese codigo: ").upper()
eliminar_juego(codigo)

