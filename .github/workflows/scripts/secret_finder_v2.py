# Crear un programa que recoja por parámetro una ruta y una palabra clave y 
# termine con error ( sys.exit(n) ) en caso de que un archivo o más en el
# directorio contenga esa palabra clave
#
# Tip 1: Comando egrep de linux, método walk de la librería os, etc.
# Tip 2: Códigos de salida con error para github
# https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions


def main():
    import subprocess as sp
    import sys
    ruta = sys.argv[1]  # esto coge el paraemtro en la poscion 1, no la 0 que es el archivo
    clave = sys.argv[2]
    resultado = sp.run(["egrep", "-R", clave, ruta], capture_output=True, text=True)
    print(resultado)
    if resultado.returncode == 0:
        print("Se an encontrado coincidencias")
        sys.exit(1)

if __name__ == "__main__":
    main()
