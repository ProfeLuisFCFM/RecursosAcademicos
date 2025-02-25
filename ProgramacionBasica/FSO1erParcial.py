import os, json, subprocess, qrcode


def install_qrcode():
    """Intenta instalar qrcode si no está disponible"""
    try:
        # Intentar importar la librería
        import qrcode
        print("✅ qrcode ya está instalado.")
    except ImportError:
        print("❌ No se encontró la librería qrcode. Procediendo con la instalación...")

        # Descargar y descomprimir el paquete desde GitHub (si no tienes pip)
        url = "https://github.com/lincolnloop/python-qrcode/archive/refs/heads/master.zip"
        zip_filename = "qrcode.zip"
        download_dir = "/tmp"  # Directorio temporal para almacenar el archivo zip

        # Descargar el archivo .zip
        subprocess.run(f"wget {url} -O {os.path.join(download_dir, zip_filename)}", shell=True)

        # Descomprimir el archivo
        subprocess.run(f"unzip {os.path.join(download_dir, zip_filename)} -d {download_dir}", shell=True)

        # Instalar el paquete sin pip (instalar desde el código fuente)
        source_dir = os.path.join(download_dir, "python-qrcode-master")
        subprocess.run(f"cd {source_dir} && python3 setup.py install", shell=True)
        
        print("✅ qrcode ha sido instalado correctamente.")

install_qrcode()

# Pedir datos del estudiante
print("Primer Examen Parcial de Fundamentos de Sistemas Operativos - Práctico")
nombre = input("Nombre: ")
matricula = input("Matrícula: ")
grupo = input("Grupo: ")

# Verificar si la carpeta y archivo existen
carpeta = os.path.expanduser("~/examen_practico")
archivo = os.path.join(carpeta, "evidencia.txt")
archivo_copia = os.path.expanduser("~/evidencia_copia.txt")

# Obtener historial de comandos
historial = subprocess.getoutput("history | tail -10")

# Obtener la IP pública del usuario
ip_publica = subprocess.getoutput("curl -s ifconfig.me")

# Guardar los resultados en un diccionario
resultados = {
    "carpeta_creada": os.path.exists(carpeta),
    "archivo_creado": os.path.exists(archivo),
    "archivo_copiado": os.path.exists(archivo_copia)
}
resultados["historial_comandos"] = historial.split("\n")
resultados["ip_publica"] = ip_publica


# Crear estructura final con datos del alumno y respuestas
examen = {
    "datos_alumno": {
        "nombre": nombre,
        "matricula": matricula,
        "grupo": grupo
    },
    "respuestas": resultados
}

# Convertir a JSON
json_examen = json.dumps(examen, indent=4)

# Generar código QR con el JSON
qr = qrcode.make(json_examen)
qr.save("resultado_qr.png")#

print("\n✅ Examen completado. Código QR generado en 'resultado_qr.png'.")

# Guardar el JSON en un archivo
'''
json_filename = "respuestas.json"
with open(json_filename, "w") as f:
    f.write(json_examen)

print("\n✅ El archivo JSON fue generado: respuestas.json")

# Comando para convertir el JSON a formato URL codificado
encoded_json = subprocess.getoutput(f"cat {json_filename} | jq -sRr @uri")

# Usar curl para generar el QR
qr_command = f"curl 'https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={encoded_json}' -o qr_code.png"
subprocess.run(qr_command, shell=True)

print("✅ QR generado: revisa el archivo qr_code.png")
'''