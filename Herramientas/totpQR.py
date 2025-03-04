import hashlib
import base64
import pyotp
import qrcode
from mnemonic import Mnemonic
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

def generate_mnemonic():
    mnemo = Mnemonic("spanish")
    words = mnemo.generate(strength=128)
    return words

def generate_totp_secret(mnemonic_words, matricula):
    words_list = mnemonic_words.split()
    if len(words_list) != 12:
        raise ValueError("Debe ingresar exactamente 12 palabras.")

    # Tomar los primeros 2 caracteres de cada palabra y concatenarlos
    partial_key = "".join(word[:2] for word in words_list)

    # Combinar con la matrícula y hacer un hash SHA256
    hashed_key = hashlib.sha256((partial_key + matricula).encode()).digest()

    # Convertir el hash a Base32 (Google Authenticator lo requiere)
    totp_secret = base64.b32encode(hashed_key).decode("utf-8").replace("=", "")[:32]

    return totp_secret

def get_google_authenticator_uri(secret_key, matricula):
    return pyotp.totp.TOTP(secret_key).provisioning_uri(name=f"Alumno-{matricula}@profeluis", issuer_name="ProfeLuis")

def generate_qr(uri):
    qr = qrcode.make(uri)
    return qr

def generate():
    matricula = entry_matricula.get().strip()
    if not matricula.isdigit() or len(matricula) < 7:
        messagebox.showerror("Error", "La matrícula debe ser un número de al menos 7 dígitos.")
        return

    mnemonic_words = generate_mnemonic()
    entry_mnemonic.delete(0, tk.END)
    entry_mnemonic.insert(0, mnemonic_words)

    secret = generate_totp_secret(mnemonic_words, matricula)
    uri = get_google_authenticator_uri(secret, matricula)
    qr = generate_qr(uri)
    
    show_qr(qr)

def recover():
    matricula = entry_matricula.get().strip()
    mnemonic_words = entry_mnemonic.get().strip()
    
    if not mnemonic_words or len(mnemonic_words.split()) != 12:
        messagebox.showerror("Error", "Debe ingresar las 12 palabras.")
        return
    if not matricula.isdigit() or len(matricula) < 7:
        messagebox.showerror("Error", "La matrícula debe ser un número de al menos 7 dígitos.")
        return

    secret = generate_totp_secret(mnemonic_words, matricula)
    uri = get_google_authenticator_uri(secret, matricula)
    qr = generate_qr(uri)
    
    show_qr(qr)

def show_qr(qr_image):
    img_byte_arr = io.BytesIO()
    qr_image.save(img_byte_arr, format="PNG")
    img_byte_arr = img_byte_arr.getvalue()
    
    img = Image.open(io.BytesIO(img_byte_arr))
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# Crear ventana
root = tk.Tk()
root.title("Clave TOTP con BIP39")
root.geometry("500x500")

# Widgets
tk.Label(root, text="Matrícula:", font=("Arial", 12)).pack()
entry_matricula = tk.Entry(root, font=("Arial", 12))
entry_matricula.pack()

tk.Label(root, text="Palabras mnemotécnicas:", font=("Arial", 12)).pack()
entry_mnemonic = tk.Entry(root, font=("Arial", 12), width=50)
entry_mnemonic.pack()

tk.Button(root, text="Generar", command=generate, font=("Arial", 12), bg="lightblue").pack(pady=5)
tk.Button(root, text="Recuperar", command=recover, font=("Arial", 12), bg="lightgreen").pack(pady=5)

qr_label = tk.Label(root)
qr_label.pack()

# Ejecutar
root.mainloop()
