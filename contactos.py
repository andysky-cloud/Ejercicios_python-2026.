def agregar_contacto():
    with open("contactos.txt", "a", encoding="utf-8") as archivo:
        identificacion = input("Identificación: ")
        nombres = input("Nombres: ")
        apellidos = input("Apellidos: ")
        correo = input("Correo: ")
        genero = input("Género: ")

        archivo.write(f"{identificacion},{nombres},{apellidos},{correo},{genero}\n")
        print("Contacto agregado correctamente\n")


def consultar_identificacion():
    buscar_id = input("Ingrese la identificación a consultar: ")
    encontrado = False

    try:
        with open("contactos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if datos[0] == buscar_id:
                    print("\nContacto encontrado:")
                    print("Identificación:", datos[0])
                    print("Nombres:", datos[1])
                    print("Apellidos:", datos[2])
                    print("Correo:", datos[3])
                    print("Género:", datos[4], "\n")
                    encontrado = True
                    break

        if not encontrado:
            print("Identificación no encontrada\n")

    except FileNotFoundError:
        print("No existen contactos registrados\n")


def listar_contactos():
    try:
        with open("contactos.txt", "r", encoding="utf-8") as archivo:
            print("\nLISTA DE CONTACTOS")
            for linea in archivo:
                datos = linea.strip().split(",")
                print(f"{datos[0]} - {datos[1]} {datos[2]} - {datos[3]} - {datos[4]}")
            print()
    except FileNotFoundError:
        print("No existen contactos registrados\n")


def menu():
    while True:
        print("Gestión de contactos")
        print("1. Agregar")
        print("2. Consultar identificación")
        print("3. Listar contactos")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        match opcion:
            case "1":
                agregar_contacto()
            case "2":
                consultar_identificacion()
            case "3":
                listar_contactos()
            case "4":
                print("Programa finalizado")
                break
            case _:
                print("Opción inválida\n")


menu()