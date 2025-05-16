import customtkinter as ctk
from tkinter import messagebox
import queue
import threading
import os
import sys
from PIL import Image
from functions.main import iniciar_conversao

# Configuração inicial
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

log_queue = queue.Queue()
running_event = threading.Event()

class QueueOutput:
    def __init__(self, log_queue):
        self.log_queue = log_queue

    def write(self, message):
        if message.strip():
            self.log_queue.put(message)

    def flush(self):
        pass

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

def update_text_widget(text_widget, log_queue):
    try:
        while True:
            message = log_queue.get_nowait()
            text_widget.configure(state='normal')
            text_widget.insert(ctk.END, message + '\n')
            text_widget.configure(state='disabled')
            text_widget.see(ctk.END)
    except queue.Empty:
        pass
    text_widget.after(500, update_text_widget, text_widget, log_queue)

def iniciar_automacao():
    try:
        threading.Thread(target=iniciar_conversao, args=(log_queue, messagebox), daemon=True).start()
    except Exception as e:
        log_queue.put(f"Erro ao iniciar a conversão: {e}")
        print(f"Erro ao iniciar a conversão: {e}")

# Criar janela
janela = ctk.CTk()
janela.title("Khrono")
largura_janela = 700
altura_janela = 500
janela.geometry(f"{largura_janela}x{altura_janela}")
janela.minsize(600, 400)

# Centralizar janela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Imagem de fundo
bg_image = None
background_label = None

try:
    bg_path = resource_path("img/Análise do Motor Dimensional.png")
    pil_image = Image.open(bg_path)

    bg_image = ctk.CTkImage(
        light_image=pil_image,
        dark_image=pil_image,
        size=(largura_janela, altura_janela)
    )

    janela.label_img = ctk.CTkLabel(master=janela, image=bg_image, text="")
    janela.label_img.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    log_queue.put(f"Erro ao carregar imagem de fundo: {e}")
    background_label = ctk.CTkLabel(janela, text="", fg_color="#2b2b2b")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Layout principal
janela.grid_rowconfigure(0, weight=2)
janela.grid_rowconfigure(1, weight=2)
janela.grid_columnconfigure(0, weight=1)

# Botão de análise
botao_analise = ctk.CTkButton(
    janela,
    text="Converter Laudos",
    fg_color="#1f538d",
    hover_color="#14375e",
    height=40,
    width=200,
    command=iniciar_automacao
)
botao_analise.grid(row=0, column=0, pady=(40, 10), sticky="n")

# Área de log
log_frame = ctk.CTkFrame(
    janela,
    fg_color="gray20",
    corner_radius=8,
    border_width=1,
    border_color="gray40"
)
log_frame.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.4)

log_box = ctk.CTkTextbox(
    log_frame,
    state="disabled",
    fg_color="transparent",
    text_color="white",
    font=("Arial", 12),
    wrap="word",
    border_width=0,
    scrollbar_button_color="gray30"
)
log_box.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

# Redimensionamento da imagem
def resize_background(event):
    if bg_image and hasattr(janela, "label_img"):
        new_width, new_height = event.width, event.height
        bg_image.configure(size=(new_width, new_height))
        janela.label_img.configure(image=bg_image)

janela.bind("<Configure>", resize_background)

# Atualização do log
update_text_widget(log_box, log_queue)

janela.mainloop()
