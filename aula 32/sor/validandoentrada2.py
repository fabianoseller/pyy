import tkinter as tk

def validar_nome():
    nome = entrada_nome.get()
    if not nome:
        rotulo_erro_nome.config(text="Campo de nome é obrigatório")
    else:
        rotulo_erro_nome.config(text="")
        rotulo_nome.config(text=f"Nome: {nome}")

def validar_genero():
    genero = entrada_genero.get()
    if not genero:
        rotulo_erro_genero.config(text="Campo de gênero é obrigatório")
    else:
        rotulo_erro_genero.config(text="")
        rotulo_genero.config(text=f"Gênero: {genero}")

def validar_idade():
    try:
        idade = int(entrada_idade.get())
        if idade > 100:
            raise ValueError("Idade acima do limite (100 anos)")
        else:
            rotulo_erro_idade.config(text="")
            rotulo_idade.config(text=f"Idade: {idade}")
    except ValueError as e:
        rotulo_erro_idade.config(text=str(e))

def validar_cidade():
    cidade = entrada_cidade.get()
    if not cidade:
        rotulo_erro_cidade.config(text="Campo de cidade é obrigatório")
    else:
        rotulo_erro_cidade.config(text="")
        rotulo_cidade.config(text=f"Cidade: {cidade}")

def validar_time():
    time = entrada_time.get()
    if not time:
        rotulo_erro_time.config(text="Campo de time é obrigatório")
    else:
        rotulo_erro_time.config(text="")
        rotulo_time.config(text=f"Time de Futebol: {time}")

janela = tk.Tk()
janela.title("Validando Entrada")

# Campo de nome
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()
botao_validar_nome = tk.Button(janela, text="Validar Nome", command=validar_nome)
botao_validar_nome.pack()
rotulo_erro_nome = tk.Label(janela, text="")
rotulo_erro_nome.pack()
rotulo_nome = tk.Label(janela, text="")
rotulo_nome.pack()

# Campo de gênero
label_genero = tk.Label(janela, text="Gênero:")
label_genero.pack()
entrada_genero = tk.Entry(janela)
entrada_genero.pack()
botao_validar_genero = tk.Button(janela, text="Validar Gênero", command=validar_genero)
botao_validar_genero.pack()
rotulo_erro_genero = tk.Label(janela, text="")
rotulo_erro_genero.pack()
rotulo_genero = tk.Label(janela, text="")
rotulo_genero.pack()

# Campo de idade
label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()
entrada_idade = tk.Entry(janela)
entrada_idade.pack()
botao_validar_idade = tk.Button(janela, text="Validar Idade", command=validar_idade)
botao_validar_idade.pack()
rotulo_erro_idade = tk.Label(janela, text="")
rotulo_erro_idade.pack()
rotulo_idade = tk.Label(janela, text="")
rotulo_idade.pack()

# Campo de cidade
label_cidade = tk.Label(janela, text="Cidade:")
label_cidade.pack()
entrada_cidade = tk.Entry(janela)
entrada_cidade.pack()
botao_validar_cidade = tk.Button(janela, text="Validar Cidade", command=validar_cidade)
botao_validar_cidade.pack()
rotulo_erro_cidade = tk.Label(janela, text="")
rotulo_erro_cidade.pack()
rotulo_cidade = tk.Label(janela, text="")
rotulo_cidade.pack()

# Campo de time
label_time = tk.Label(janela, text="Time de Futebol:")
label_time.pack()
entrada_time = tk.Entry(janela)
entrada_time.pack()
botao_validar_time = tk.Button(janela, text="Validar Time", command=validar_time)
botao_validar_time.pack()
rotulo_erro_time = tk.Label(janela, text="")
rotulo_erro_time.pack()
rotulo_time = tk.Label(janela, text="")
rotulo_time.pack()

janela.mainloop()