import tkinter as tk

def contar_caracteres(texto):
    return len(texto)

def contar_letras(texto):
    letras = 0
    for char in texto:
        if char.isalpha():
            letras += 1
    return letras

def salvar_texto_em_arquivo(texto, arquivo_nome):
    try:
        with open(arquivo_nome, "w") as arquivo:
            arquivo.write(texto)
        print("O texto foi salvo com sucesso no arquivo", arquivo_nome)
    except Exception as e:
        print("Erro ao salvar o texto no arquivo:", str(e))

def carregar_texto_de_arquivo(campo_texto, arquivo_nome):
    try:
        with open(arquivo_nome, "r") as arquivo:
            texto = arquivo.read()
        campo_texto.delete(1.0, tk.END)
        campo_texto.insert(tk.END, texto)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print("Erro ao carregar o texto do arquivo:", str(e))

def fechar_janela():
    janela.destroy()

# Criar janela
janela = tk.Tk()
janela.title("Exercício de Texto")

# Criar campos de texto
campo_texto = tk.Text(janela, height=10, width=40)
campo_texto.pack()

# Criar botões
botao_salvar = tk.Button(janela, text="Salvar", command=lambda: salvar_texto_em_arquivo(campo_texto.get("1.0", tk.END), "texto_salvo.txt"))
botao_salvar.pack()

botao_carregar = tk.Button(janela, text="Carregar", command=lambda: carregar_texto_de_arquivo(campo_texto, "texto_salvo.txt"))
botao_carregar.pack()

botao_fechar = tk.Button(janela, text="Fechar", command=fechar_janela)
botao_fechar.pack()

# Criar label para exibir contagem de caracteres
label_caracteres = tk.Label(janela, text="")
label_caracteres.pack()

# Criar label para exibir contagem de letras
label_letras = tk.Label(janela, text="")
label_letras.pack()

# Função para atualizar contagem de caracteres
def atualizar_contagem_caracteres():
    texto = campo_texto.get("1.0", tk.END)
    label_caracteres.config(text=f"Contagem de caracteres: {contar_caracteres(texto)}")

# Função para atualizar contagem de letras
def atualizar_contagem_letras():
    texto = campo_texto.get("1.0", tk.END)
    label_letras.config(text=f"Contagem de letras: {contor_letras(texto)}")

# Atualizar contagem de caracteres e letras
campo_texto.bind("<KeyRelease>", atualizar_contagem_caracteres)
campo_texto.bind("<KeyRelease>", atualizar_contagem_letras)

# Iniciar janela
janela.mainloop()
