import tkinter as tk

janela = tk.Tk()
janela.title("Criando Menus")

barra_menu = tk.Menu(janela)

menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Abrir")
menu_arquivo.add_command(label="Salvar")
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Copiar")
menu_editar.add_command(label="Colar")
barra_menu.add_cascade(label="Editar", menu=menu_editar)

menu_ajuda = tk.Menu(barra_menu, tearoff=0)
menu_ajuda.add_command(label="Sobre")
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

janela.config(menu=barra_menu)
janela.mainloop()