import tkinter as tk#Este comando importa o módulo Tkinter e o renomeia para tk. Isso significa que podemos usar tk para acessar as classes e funções do Tkinter em vez do nome completo.

janela = tk.Tk()#Esta linha cria uma instância da classe Tk(), que representa a janela principal da interface gráfica. A variável janela armazena uma referência a essa instância.
janela.title("Minha Janela Personalizada")#Este comando define o título da janela principal como "Minha Janela Personalizada". O título é exibido na barra de título da janela.
janela.geometry("400x300")#Esta linha define o tamanho da janela principal para 400 pixels de largura e 300 pixels de altura. As dimensões são especificadas no formato "largura_em_pixelsxaltura_em_pixels".
janela.geometry("+200+100")#Este comando define a posição da janela principal na tela. Os valores "+200" e "+100" indicam que a janela deve ser posicionada 200 pixels à direita e 100 pixels acima da borda superior esquerda da tela.

rotulo = tk.Label(janela, text="Olá, Mundo!")#Esta linha cria uma instância da classe Label(), que representa um rótulo de texto na interface gráfica. O rótulo é associado à janela principal (janela) e o texto "Olá, Mundo!" é definido como seu conteúdo. A variável rotulo armazena uma referência a essa instância.
rotulo.pack(pady=20)#Este comando posiciona o rótulo na janela principal. O método pack() é usado para organizar os widgets na janela. O parâmetro pady=20 especifica que deve haver um espaço de 20 pixels acima e abaixo do rótulo.

botao = tk.Button(janela, text="Clique em Mim")#Esta linha cria uma instância da classe Button(), que representa um botão clicável na interface gráfica. O botão é associado à janela principal (janela) e o texto "Clique em Mim" é definido como seu rótulo. A variável botao armazena uma referência a essa instância.
botao.pack(pady=20)#Este comando posiciona o botão na janela principal. O método pack() é usado para organizar os widgets na janela. O parâmetro pady=20 especifica que deve haver um espaço de 20 pixels acima e abaixo do botão.

janela.mainloop()#Este comando inicia o loop principal da interface gráfica. O loop principal fica à espera de eventos do usuário, como cliques de mouse e pressionamentos de teclas, e atualiza a interface de acordo com esses eventos. A interface gráfica permanece aberta enquanto o loop principal estiver em execução.