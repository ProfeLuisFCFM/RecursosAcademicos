import os
import json

def verificar_comandos():

    # Pedir datos del estudiante
    print("Primer Examen Parcial de Fundamentos de Sistemas Operativos - Práctico")
    nombre = input("Nombre: ")
    matricula = input("Matrícula: ")
    grupo = input("Grupo: ")


    resultados = {}

    # Actividad 1
    resultados["directorio_creado"] = os.path.isdir("prueba")
    resultados["archivo_creado"] = os.path.isfile("prueba/archivo.txt")
    resultados["archivo_movido"] = not os.path.isfile("prueba/copia.txt") and os.path.isfile("prueba/movido.txt")
    
    # Actividad 2
    if os.path.isfile("prueba/mensaje.txt"):
        with open("prueba/mensaje.txt", "r") as f:
            resultados["mensaje_correcto"] = f.read().strip() == "Hola mundo"

    # Actividad 3
    resultados["pwd_correcto"] = os.getcwd()

    # Actividad 4
    resultados["proceso_bash"] = os.system("ps aux | grep bash > /dev/null") == 0

    # Actividad 5 - Listar archivos y verificar tamaño
    resultados["lista_archivos"] = os.listdir("prueba") if os.path.isdir("prueba") else []
    resultados["tamano_archivos"] = {f: os.path.getsize(os.path.join("prueba", f)) for f in resultados["lista_archivos"]}

    # Actividad 6 - Contar líneas en un archivo de log
    if os.path.isfile("prueba/log.txt"):
        with open("prueba/log.txt", "r") as f:
            resultados["lineas_log"] = len(f.readlines())
    else:
        resultados["lineas_log"] = 0

    examen = {
        "datos_alumno": {
            "nombre": nombre,
            "matricula": matricula,
            "grupo": grupo
        },
        "respuestas": resultados
    }
    # Guardar resultados en JSON
    with open("resultados.json", "w") as f:
        json.dump(examen, f, indent=4)

    print("✅ Verificación completada. Archivo 'resultados.json' generado.")

if __name__ == "__main__":
    verificar_comandos()
