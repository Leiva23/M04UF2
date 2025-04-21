def show_menu():
    while True:
        print("- Menu Principal -")
        print("1. Albunes")
        print("2. Artistas")
        print("3. Canciones")
        print("4. Generos")
        print("0. Salir")
        
        choice = int(input("Seleccione una opcion: "))
        
        if choice == 1:
            show_menu_albums()
        elif choice == 2:
            show_menu_artists()
        elif choice == 3:
            show_menu_songs()
        elif choice == 4:
            show_menu_genres()
        elif choice == 0:
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida. Por favor, elija una opcion entre 0 y 4.")
            

def show_menu_albums():
    while True:
        print("- Menu de Albunes -")
        print("1. Listar todos los albunes")
        print("2. Buscar album por titulo")
        print("0. Volver")
        
        choice = int(input("Seleccione una opcion: "))
        
        if choice == 1:
            print("Listando todos los albunes...")
        elif choice == 2:
            print("Buscando album por titulo...")
        elif choice == 0:
            break
        else:
            print("Opcion no valida. Por favor, elija una opcion entre 0 y 2.")
        

def show_menu_artists():
    while True:
        print("- Menu de Artistas -")
        print("1. Listar todos los artistas")
        print("2. Buscar artista por nombre")
        print("0. Volver")
        
        choice = int(input("Seleccione una opcion: "))
        
        if choice == 1:
            print("Listando todos los artistas...")
        elif choice == 2:
            print("Buscando artista por nombre...")
        elif choice == 0:
            break
        else:
            print("Opcion no valida. Por favor, elija una opcion entre 0 y 2.")

def show_menu_songs():
    while True:
        print("- Menu de Canciones -")
        print("1. Listar todas las canciones")
        print("2. Buscar cancion por titulo")
        print("0. Volver")
        
        choice = int(input("Seleccione una opcion: "))
        
        if choice == 1:
            print("Listando todas las canciones...")
        elif choice == 2:
            print("Buscando cancion por titulo...")
        elif choice == 0:
            break
        else:
            print("Opcion no valida. Por favor, elija una opcion entre 0 y 2.")

def show_menu_genres():
    while True:
        print("- Menu de Generos -")
        print("1. Listar todos los generos")
        print("2. Buscar genero por nombre")
        print("0. Volver")
        
        choice = int(input("Seleccione una opcion: "))
        
        if choice == 1:
            print("Listando todos los generos...")
        elif choice == 2:
            print("Buscando genero por nombre...")
        elif choice == 0:
            break
        else:
            print("Opcion no valida. Por favor, elija una opcion entre 0 y 2.")
