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

def carregar_texto_de_arquivo(arquivo_nome):
    try:
        with open(arquivo_nome, "r") as arquivo:
            texto = arquivo.read()
        return texto
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return ""
    except Exception as e:
        print("Erro ao carregar o texto do arquivo:", str(e))
        return ""

janela = tk.Tk()
janela.title("Exercício de Texto")

campo_texto = tk.Text(janela, height=10, width=40)
campo_texto.pack()

botao_salvar = tk.Button(janela, text="Salvar", command=lambda: salvar_texto_em_arquivo(campo_texto.get("1.0", tk.END), "texto_salvo.txt"))
botao_salvar.pack()

botao_carregar = tk.Button(janela, text="Carregar", command=lambda: campo_texto.delete(1.0, tk.END) or campo_texto.insert(tk.END, carregar_texto_de_arquivo("texto_salvo.txt")))
botao_carregar.pack()

# contagem de caracteres
label_caracteres = tk.Label(janela, text="Contagem de caracteres: 0")
label_caracteres.pack()

# contagem de letras
label_letras = tk.Label(janela, text="Contagem de letras: 0")
label_letras.pack()

# contagem de caracteres
contagem_caracteres = 0
contagem_letras = 0

def atualizar_contagem_caracteres():
    global contagem_caracteres
    texto = campo_texto.get("1.0", tk.END)
    contagem_caracteres = contar_caracteres(texto)
    label_caracteres.config(text=f"Contagem de caracteres: {contagem_caracteres}")

def atualizar_contagem_letras():
    global contagem_letras
    texto = campo_texto.get("1.0", tk.END)
    contagem_letras = contar_letras(texto)
    label_letras.config(text=f"Contagem de letras: {contagem_letras}")

# Atualizar contagem de caracteres e letras
campo_texto.bind("<KeyRelease>", atualizar_contagem_caracteres)
campo_texto.bind("<KeyRelease>", atualizar_contagem_letras)

# Iniciar janela
janela.mainloop()
