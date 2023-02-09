import qrcode
import tkinter as tk
from tkinter import Button, Entry

def generate_qrcode():
    # Obtém o conteúdo a ser codificado no QR code
    data = entry.get()

    # Cria o QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Salva o QR code como uma imagem
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

    # Ativa o botão de download
    download_button.config(state="normal")

def download_image():
    # Adicione o código para fazer o download da imagem aqui
    pass

# Cria a janela principal
root = tk.Tk()
root.title("Gerador de QR Code")

# Cria o campo de texto
entry = Entry(root)
entry.pack()

# Cria o botão "Gerar QR code"
generate_button = Button(root, text="Gerar QR Code", command=generate_qrcode)
generate_button.pack()

# Cria o botão "Download", inicialmente desabilitado
download_button = Button(root, text="Download", command=download_image, state="disabled")
download_button.pack()

# Inicia a interface gráfica de usuário
root.mainloop()