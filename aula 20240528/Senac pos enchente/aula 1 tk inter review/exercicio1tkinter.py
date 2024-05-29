
import tkinter as tk
from tkinter import messagebox

# RESPOSTA DO EXERCICIO >>> Criar a janela principal
root = tk.Tk()
root.title("Meu Programa")
root.geometry("300x200")
root.resizable(False, False)

# RESPOSTA DO EXERCICIO >>> Criar um rótulo e um botão
label = tk.Label(root, text="Olá, Mundo!")
label.pack()
button = tk.Button(root, text="Clique em Mim")
button.pack()

# RESPOSTA DO EXERCICIO >>> Criar um campo de entrada de texto e um botão
name_label = tk.Label(root, text="Nome:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()
show_button = tk.Button(root, text="Mostrar Nome")
show_button.pack()

# RESPOSTA DO EXERCICIO >>> Criar um botão para alterar a cor do rótulo
color_button = tk.Button(root, text="Clique para Mudar Cor")
color_button.pack()
color_label = tk.Label(root, text="Cor", fg="red")
color_label.pack()

# RESPOSTA DO EXERCICIO >>> Criar um checkbox para controlar a visibilidade do texto
check_var = tk.IntVar()
check_var.set(0)
check_button = tk.Checkbutton(root, text="Mostrar texto", variable=check_var)
check_button.pack()
text_label = tk.Label(root, text="Este texto será mostrado se o checkbox estiver marcado.")
text_label.pack()

# RESPOSTA DO EXERCICIO >>> Criar radio buttons para escolher uma opção
radio_var = tk.IntVar()
radio_var.set(1)
radio1 = tk.Radiobutton(root, text="Opção 1", variable=radio_var, value=1)
radio1.pack()
radio2 = tk.Radiobutton(root, text="Opção 2", variable=radio_var, value=2)
radio2.pack()
radio3 = tk.Radiobutton(root, text="Opção 3", variable=radio_var, value=3)
radio3.pack()
selected_label = tk.Label(root, text="Opção selecionada: ")
selected_label.pack()

# RESPOSTA DO EXERCICIO >>> Funções para manipular as interações do usuário
def show_name():
    name = name_entry.get()
    messagebox.showinfo("Nome", name)

def change_color():
    if color_label.cget("fg") == "red":
        color_label.config(fg="green")
    else:
        color_label.config(fg="red")

def show_text():
    if check_var.get() == 1:
        text_label.pack()
    else:
        text_label.pack_forget()

def show_selected():
    selected = radio_var.get()
    if selected == 1:
        selected_label.config(text="Opção 1 selecionada.")
    elif selected == 2:
        selected_label.config(text="Opção 2 selecionada.")
    else:
        selected_label.config(text="Opção 3 selecionada.")

# RESPOSTA DO EXERCICIO >>> Configurar as funções para os botões
button.config(command=show_name)
show_button.config(command=show_name)
color_button.config(command=change_color)
check_button.config(command=show_text)
radio1.config(command=show_selected)
radio2.config(command=show_selected)
radio3.config(command=show_selected)

# RESPOSTA DO EXERCICIO >>> Iniciar a janela
root.mainloop()

