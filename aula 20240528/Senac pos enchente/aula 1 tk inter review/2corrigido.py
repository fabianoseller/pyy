import tkinter as tk#Este comando importa o módulo Tkinter e o renomeia para tk. Isso significa que podemos usar tk para acessar as classes e funções do Tkinter em vez do nome completo.

def mostrar_nome():#Esta função é chamada quando o botão "Mostrar Nome" é clicado.
  nome_digitado = campo_nome.get()#A função obtém o texto digitado no campo de entrada campo_nome e o armazena na variável nome_digitado.
  rotulo_nome.config(text=f"Nome: {nome_digitado}")#A função configura o texto do rótulo rotulo_nome para "Nome: " seguido do nome digitado. O prefixo f antes da string permite formatação de string, inserindo o valor da variável nome_digitado na string.

janela = tk.Tk()#Esta linha cria uma instância da classe Tk(), que representa a janela principal da interface gráfica.
janela.title("Entrada e Exibição de Nome")#A variável janela armazena uma referência a essa instância.O título da janela é definido como "Entrada e Exibição de Nome".
 

rotulo_instrucao = tk.Label(janela, text="Digite seu nome:")#Esta linha cria uma instância da classe Label(), que representa um rótulo de texto na interface gráfica. O rótulo é associado à janela principal (janela) e o texto "Digite seu nome:" é definido como seu conteúdo. A variável rotulo_instrucao armazena uma referência a essa instância.
rotulo_instrucao.pack(pady=10)#O método pack() é usado para posicionar o rótulo na janela. O parâmetro pady=10 especifica que deve haver um espaço de 10 pixels acima e abaixo do rótulo.




campo_nome = tk.Entry(janela)#Esta linha cria uma instância da classe Entry(), que representa um campo de entrada de texto na interface gráfica.
# O campo de entrada é associado à janela principal (janela). A variável campo_nome armazena uma referência a essa instância.
campo_nome.pack(pady=10)#O método pack() é usado para posicionar o campo de entrada na janela. O parâmetro pady=10 especifica que deve haver um espaço de 10 pixels acima e abaixo do campo de entrada.

rotulo_nome = tk.Label(janela, text="")  # Texto inicial vazio
#Esta linha cria uma instância da classe Label(), que representa um rótulo de texto na interface gráfica. O rótulo é associado à janela principal (janela) e o texto inicial é definido como vazio. A variável rotulo_nome armazena uma referência a essa instância.
rotulo_nome.pack(pady=10)#O método pack() é usado para posicionar o rótulo na janela. O parâmetro pady=10 especifica que deve haver um espaço de 10 pixels acima e abaixo do rótulo.


botao_mostrar = tk.Button(janela, text="Mostrar Nome", command=mostrar_nome)#Esta linha cria uma instância da classe Button(), que representa um botão clicável na interface gráfica. O botão é associado à janela principal (janela) e o texto "Mostrar Nome" é definido como seu rótulo. A variável botao_mostrar armazena uma referência a essa instância.
#O parâmetro command=mostrar_nome especifica que a função mostrar_nome deve ser chamada quando o botão for clicado.
botao_mostrar.pack(pady=10)#O método pack() é usado para posicionar o botão na janela. O parâmetro pady=10 especifica que deve haver um espaço de 10 pixels acima

janela.mainloop()#Este comando inicia o loop principal da interface gráfica. O loop principal fica à espera de eventos do usuário, como cliques de mouse e pressionamentos de teclas, e atualiza a interface de acordo com esses eventos. A interface gráfica permanece aberta enquanto o loop principal estiver em execução.