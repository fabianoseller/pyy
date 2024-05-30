import tkinter as tk#Este comando importa o módulo Tkinter e o renomeia para tk. Isso significa que podemos usar tk para acessar as classes e funções do Tkinter em vez do nome completo.


def alternar_cor():#Esta função é responsável por alternar a cor do fundo do rótulo.
  #A função declara as variáveis cor_atual e nova_cor como global, o que significa que elas podem ser acessadas e modificadas em qualquer lugar dentro da função, mesmo que sejam definidas em outro escopo.
  global cor_atual, nova_cor

  if cor_atual == "red":#Um bloco if verifica se a cor_atual é igual a "red".Se for verdade, a cor_atual é definida como nova_cor.
    cor_atual = nova_cor#Se for falso, a cor_atual é definida como "red".
  else:
    cor_atual = "red"
#A função configura a cor de fundo do rotulo para a cor_atual.
  rotulo.config(bg=cor_atual)

janela = tk.Tk()#Esta linha cria uma instância da classe Tk(), que representa a janela principal da interface gráfica. A variável janela armazena uma referência a essa instância.
janela.title("Alternador de Cor")#O título da janela é definido como "Alternador de Cor".

#Estas linhas definem duas variáveis:
cor_atual = "red"#cor_atual: Armazena a cor atual do fundo do rótulo, inicialmente definida como "red".
nova_cor = "green"#nova_cor: Armazena a cor que será alternada para o fundo do rótulo, inicialmente definida como "green".

rotulo = tk.Label(janela, text="Texto Vermelho", bg=cor_atual)#Esta linha cria uma instância da classe Label(), que representa um rótulo de texto na interface gráfica. O rótulo é associado à janela principal (janela), o texto "Texto Vermelho" é definido como seu conteúdo e a cor de fundo é definida como cor_atual (que é "red" neste caso). A variável rotulo armazena uma referência a essa instância.
rotulo.pack(pady=20)#O método pack() é usado para posicionar o rótulo na janela. O parâmetro pady=20 especifica que deve haver um espaço de 20 pixels acima e abaixo do rótulo.

botao = tk.Button(janela, text="Clique para Mudar Cor", command=alternar_cor)#Esta linha cria uma instância da classe Button(), que representa um botão clicável na interface gráfica. O botão é associado à janela principal (janela) e o texto "Clique para Mudar Cor" é definido como seu rótulo. A variável botao armazena uma referência a essa instância.
#O parâmetro command=alternar_cor especifica que a função alternar_cor deve ser chamada quando o botão for clicado.
botao.pack(pady=20)#O método pack() é usado para posicionar o botão na janela. O parâmetro pady=20 especifica que deve haver um espaço de 20 pixels acima e abaixo do botão.

janela.mainloop()#Este comando inicia o loop principal da interface gráfica. O loop principal fica à espera de eventos do usuário, como cliques de mouse e pressionamentos de teclas, e atualiza a interface de acordo com esses eventos. A interface gráfica permanece aberta enquanto o loop principal estiver em execução.