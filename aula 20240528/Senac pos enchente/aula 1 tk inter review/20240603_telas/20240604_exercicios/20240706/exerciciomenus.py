import tkinter as tk
from tkinter import filedialog
import sys

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Exemplo de aprendizado menus >>> janela principal com título
        self.title("Meu Programa")

        # Exemplo de aprendizado menus >>> menu principal
        self.menu_principal = tk.Menu(self)

        # Exemplo de aprendizado menus >>> item principal
        self.menu_principal.add_cascade(label="Arquivo", menu=self.create_submenu_arquivo())

        # Exemplo de aprendizado menus >>> submenu "Arquivo"
        self.submenu_arquivo = tk.Menu(self.menu_principal, tearoff=0)
        self.submenu_arquivo.add_command(label="Novo", command=lambda: print("Novo arquivo"), state=tk.NORMAL)
        self.submenu_arquivo.add_command(label="Abrir", command=self.abrir_arquivo, state=tk.NORMAL)
        self.submenu_arquivo.add_separator()
        self.submenu_arquivo.add_command(label="Desfazer", command=lambda: print("Desfazer"), state=tk.DISABLED)
        self.menu_principal.add_cascade(label="Arquivo", menu=self.submenu_arquivo)

        # Exemplo de aprendizado menus >>> submenu "Editar"
        self.submenu_editar = tk.Menu(self.menu_principal, tearoff=0)
        self.submenu_editar.add_command(label="Copiar", command=lambda: print("Copiar"))
        self.submenu_editar.add_command(label="Conteúdo", command=lambda: print("Conteúdo"))
        self.menu_principal.add_cascade(label="Editar", menu=self.submenu_editar)

        # Exemplo de aprendizado menus >>> submenu "Ajuda"
        self.submenu_ajuda = tk.Menu(self.menu_principal, tearoff=0)
        self.submenu_ajuda.add_command(label="Sobre", command=lambda: print("Sobre"))
        self.menu_principal.add_cascade(label="Ajuda", menu=self.submenu_ajuda)

        # Exemplo de aprendizado menus >>> variável para controlar o estado das opções
        self.estado_opcoes = tk.BooleanVar()
        self.estado_opcoes.set(True)

        # Exemplo de aprendizado menus >>> Adicionar item ao menu para alternar o estado das opções
        self.menu_principal.add_checkbutton(label="Ativar/Desativar Opções", variable=self.estado_opcoes, command=self.alternar_estado_opcoes)

        # Exemplo de aprendizado menus >>> item de sair
        self.menu_principal.add_command(label="Sair", command=self.fechar)

        # Exemplo de aprendizado menus >>> item de fechar
        self.menu_principal.add_command(label="Fechar", command=self.fechar)

        # Adicionar menu principal à janela
        self.config(menu=self.menu_principal)

    def alternar_estado_opcoes(self):
        if self.estado_opcoes.get():
            self.submenu_arquivo.entryconfig("Novo", state=tk.NORMAL)
            self.submenu_arquivo.entryconfig("Abrir", state=tk.NORMAL)
            self.submenu_arquivo.entryconfig("Desfazer", state=tk.DISABLED)
        else:
            self.submenu_arquivo.entryconfig("Novo", state=tk.DISABLED)
            self.submenu_arquivo.entryconfig("Abrir", state=tk.DISABLED)
            self.submenu_arquivo.entryconfig("Desfazer", state=tk.NORMAL)

    def create_submenu_arquivo(self):
        submenu_arquivo = tk.Menu(self.menu_principal, tearoff=0)
        submenu_arquivo.add_command(label="Novo", command=lambda: print("Novo arquivo"), state=tk.NORMAL)
        submenu_arquivo.add_command(label="Abrir", command=self.abrir_arquivo, state=tk.NORMAL)
        submenu_arquivo.add_separator()
        submenu_arquivo.add_command(label="Desfazer", command=lambda: print("Desfazer"), state=tk.DISABLED)
        return submenu_arquivo

    def abrir_arquivo(self):
        arquivo_nome = filedialog.askopenfilename(title="Selecione um arquivo", filetypes=[("Arquivos de texto", "*.txt")])
        if arquivo_nome:
            with open(arquivo_nome, "r") as arquivo:
                print("Arquivo aberto:", arquivo_nome)
                print("Conteúdo do arquivo:")
                print(arquivo.read())

    def fechar(self):
        sys.exit()

if __name__ == "__main__":
    app = App()
    app.mainloop()
