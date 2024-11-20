################################################################################
# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema" 
# sino se da un error.
# ################################################################################

usuario = input("\nIntroduce tu nombre de usuario: ")
contra = input("Introduce tu contraseña: ")

if usuario == "pepe" and contra == "asdasd":
    print("\nHas entrado al sistema")
else:
    print("\nError: Usuario o contraseña incorrectos")
