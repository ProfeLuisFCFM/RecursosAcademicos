import os
import json
import subprocess
import qrcode

def install_qrcode():
    try:
        import qrcode
    except ImportError:
        print("Instalando la librería qrcode...")
        subprocess.check_call(["pip", "install", "qrcode[pil]"])
        import qrcode  # Importar nuevamente tras la instalación

def generate_qr_from_json(json_filename):
    if not os.path.exists(json_filename):
        print(f"Error: El archivo {json_filename} no existe.")
        return
    
    with open(json_filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    json_string = json.dumps(data)
    
    qr = qrcode.make(json_string)
    output_filename = "qr_resultados.png"
    qr.save(output_filename)
    print(f"Código QR generado y guardado como {output_filename}")

if __name__ == "__main__":
    install_qrcode()
    generate_qr_from_json("resultados.json")
