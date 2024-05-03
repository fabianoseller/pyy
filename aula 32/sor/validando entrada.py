import tkinter as tk

def validar_idade():
    try:
        idade = int(entrada_idade.get())
        if idade > 100:
            raise ValueError("Idade acima do limite (100 anos)")
        else:
            rotulo_erro.config(text="")
    except ValueError as e:
        rotulo_erro.config(text=str(e))

janela = tk.Tk()
janela.title("Validando Entrada")

entrada_idade = tk.Entry(janela)
entrada_idade.pack()

botao_validar = tk.Button(janela, text="Validar Idade", command=validar_idade)
botao_validar.pack()

rotulo_erro = tk.Label(janela, text="")
rotulo_erro.pack()

janela.mainloop()