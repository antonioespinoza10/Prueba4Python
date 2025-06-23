
usuarios = []

def menu():
    print("1.-Ingresar Usuario.")
    print("2.-Buscar Usuario.")
    print("3.-Eliminar.")
    print("4.-Salir")
    opc = input("Ingrese opcion: ")
    return opc

def inventario():
    if len(usuarios) == 0:
        print("Error, no hay productos en inventario!.")
        return 0
    else:
        return 1
    
def datos():
    usuario = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (M/F): ")
    contraseña = input("Ingrese su contraseña: ")
    
    if usuario in usuarios:
        print("Usuario ya existe. Intente otro")
    elif sexo not in ['M', 'F']:
        print("Debe ingresar M o F solamente. Intente de nuevo")
    elif len(contraseña) < 6:
        print("Contraseña no válida. Debe tener al menos 6 caracteres. Intente con otra")
    else:
        usuarios.append(usuario)
        print("Usuario ingresado con éxito!!")  

def buscar():
    opcion = inventario() 
    if opcion == 0:
        return 0
    usuario = input("Ingrese el nombre de usuario a buscar: ")
    for i in usuarios:
        if i == usuario:
            print("Usuario encontrado:", i)
            return
    print("Usuario no encontrado")  
    
def eliminar():
    opcion = inventario()
    if opcion == 0:
        return 0
    usuario = input("Ingrese el nombre de usuario a eliminar: ")
    for i in usuarios:
        if i == usuario:
            usuarios.remove(i)
            print("usuario eliminado con exito")
            return
        print("usuario no encontrado")

usuarios = []

def main():
    while True:
        opc = menu()
        if opc == "1":
            datos()
        elif opc == "2":
            buscar()
        elif opc == "3":
            eliminar()
        elif opc == "4":
            break
        else:
            print("opcion no valida intente de nuevo")
if __name__ == "__main__":
    main()  

        













