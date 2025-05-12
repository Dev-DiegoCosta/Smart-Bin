# Smart-Bin
Smart Bin

import tkinter as tk
from tkinter import simpledialog, messagebox
from utils_qrcode import gerar_qr_code
from data_store import cadastrar_usuario, adicionar_pontos, get_pontos
from config import PONTOS_POR_DESCARTE, COR_FUNDO, COR_TEXTO


def centralizar_janela(tela, largura, altura):
    tela.update_idletasks()
    largura_tela = tela.winfo_screenwidth()
    altura_tela = tela.winfo_screenheight()
    pos_x = largura_tela // 2 - largura // 2
    pos_y = altura_tela // 2 - altura // 2
    tela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')


def tela_descarte(cpf):
    descarte = tk.Toplevel(root)
    descarte.title("Descarte de Lixo")
    centralizar_janela(descarte, 800, 800)
    descarte.configure(bg=COR_FUNDO)

    titulo = tk.Label(descarte, text="🗑️ Simulação de Descarte 🗑️", font=("Arial", 26, "bold"), bg=COR_FUNDO, fg=COR_TEXTO)
    titulo.pack(pady=30)

    subtitulo = tk.Label(descarte, text="Clique no botão abaixo para descartar!", font=("Arial", 16), bg=COR_FUNDO, fg="#00008B")
    subtitulo.pack(pady=10)

    def descartar():
        adicionar_pontos(cpf, PONTOS_POR_DESCARTE)
        total = get_pontos(cpf)
        messagebox.showinfo("Sucesso!", f"✅ Você ganhou {PONTOS_POR_DESCARTE} pontos!\nTotal de pontos: {total} pontos.")
        descarte.destroy()

    botao_descartar = tk.Button(descarte, text="Descartar Lixo", font=("Arial", 20, "bold"), bg=COR_TEXTO, fg="white", width=15, height=2, command=descartar)
    botao_descartar.pack(pady=100)


def tela_cadastrar_cpf():
    cpf = simpledialog.askstring("Cadastro", "Digite seu CPF (apenas números):")
    if cpf:
        novo = cadastrar_usuario(cpf)
        if novo:
            messagebox.showinfo("Bem-vindo!", "✅ CPF cadastrado com sucesso!")
        else:
            pontos = get_pontos(cpf)
            messagebox.showinfo("Bem-vindo de volta!", f"🎉 Você já tem {pontos} pontos!")
        tela_descarte(cpf)
    else:
        messagebox.showwarning("Erro", "CPF não informado.")


# Criação da janela principal
root = tk.Tk()
root.title("Lixeira Inteligente - São João 2025")
largura = 800
altura = 800
centralizar_janela(root, largura, altura)
root.configure(bg=COR_FUNDO)

# Título
titulo = tk.Label(root, text="🎉 Lixeira Inteligente 🎉", font=("Arial", 26, "bold"), bg=COR_FUNDO, fg=COR_TEXTO)
titulo.pack(pady=30)

# Subtítulo
subtitulo = tk.Label(root, text="Descartou? Ganhou pontos e concorre a prêmios!", font=("Arial", 16), bg=COR_FUNDO, fg="#00008B")
subtitulo.pack(pady=10)

# Área do QR Code genérico
qr_frame = tk.Frame(root, bg="white", width=250, height=250, highlightbackground="black", highlightthickness=2)
qr_frame.pack(pady=40)

# Gerar QR genérico
qr_img = gerar_qr_code("default")
if qr_img:
    qr_label = tk.Label(qr_frame, image=qr_img, bg="white")
    qr_label.image = qr_img
    qr_label.place(relx=0.5, rely=0.5, anchor="center")

# Botão de Cadastro
botao_cadastrar = tk.Button(root, text="Cadastrar/Entrar com CPF", font=("Arial", 18, "bold"), bg=COR_TEXTO, fg="white", width=25, height=2, command=tela_cadastrar_cpf)
botao_cadastrar.pack(pady=40)

# Rodapé
rodape = tk.Label(root, text="Obrigado por fazer parte de um São João mais sustentável! ♻️", font=("Arial", 12), bg=COR_FUNDO, fg="green")
rodape.pack(side="bottom", pady=20)

root.mainloop()
