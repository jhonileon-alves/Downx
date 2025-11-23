from customtkinter import *
from tkinter.filedialog import askdirectory
from yt_dlp import *

# Inicialização
set_appearance_mode("dark")
set_default_color_theme("blue")

root = CTk()
root.title('DownX')
root.geometry('650x430')
root.resizable(False, False)
root.iconbitmap("downx.ico")

pastaDestinada = ""

def destino():
    global pastaDestinada
    caminho = askdirectory()
    if caminho == "":
        status.configure(text="Nenhuma pasta selecionada", text_color="red")
        return
    pastaDestinada = caminho
    status.configure(status.configure(text=f"Caminho selecionado: {pastaDestinada}", text_color="lightgreen"))

def baixarVideo():
    if not pastaDestinada:
        status.configure(text="Escolha uma pasta primeiro!", text_color="yellow")
        return

    url = entradaUrl.get().strip()
    if not url:
        status.configure(text='Digite um URL', text_color='yellow')
        return

    root.update()

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": pastaDestinada + "/%(title)s.%(ext)s"
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status.configure(text="Download concluído!", text_color="lightgreen")
    except Exception as e:
        status.configure(text=f"Erro: {e}", text_color="red")

# TÍTULO
CTkLabel(root, text='DownX', font=('Impact', 80)).pack(pady=10)

# FRAME PRINCIPAL
frame = CTkFrame(root)
frame.pack(pady=20)

# Texto URL
texto1 = CTkLabel(frame, text='Copie a URL do vídeo:', font=('Impact', 15))
texto1.grid(row=0, column=0, padx=10, pady=10)

# Entrada
entradaUrl = CTkEntry(frame, width=300, font=("Arial", 12))
entradaUrl.grid(row=0, column=1, padx=10)

# Botões
butaoDestino = CTkButton(frame, text='Escolher pasta', width=150, command=destino)
butaoDestino.grid(row=1, column=0, padx=10, pady=20)

butaoDownload = CTkButton(frame, text='Download', width=150, command=baixarVideo)
butaoDownload.grid(row=1, column=1, padx=10, pady=20)

# Status
statusFrame = CTkFrame(root)
statusFrame.pack(side=BOTTOM, fill=X, pady=10)

CTkLabel(statusFrame, text="STATUS:", font=('Impact', 15)).pack(side=LEFT, padx=10)
status = CTkLabel(statusFrame, text="Aguardando...", font=('Impact', 15))
status.pack(side=LEFT)

# Criador
statusFrame.pack(side=BOTTOM, fill=X, pady=10)

CTkLabel(statusFrame, text="By: Jhoni", font=('Impact', 15)).pack(side=RIGHT, padx=10)

status.pack(side=LEFT)
root.mainloop()
