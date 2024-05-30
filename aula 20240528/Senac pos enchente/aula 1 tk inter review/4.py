import tkinter as tk#Este comando importa o módulo Tkinter e o renomeia para tk. Isso significa que podemos usar tk para acessar as classes e funções do Tkinter em vez do nome completo.


def mostrar_texto():#Esta função é responsavel por ocultar ou não o texto.
  if var_checkbox.get():#Verifica se o checkbox está marcado (var_checkbox.get() retorna True se marcado, False se não marcado).
#Se marcado:#Define o texto do rótulo rotulo_texto como "Texto Oculto".
    rotulo_texto.config(text="Texto Oculto")
  else:#Se o checkbox não estiver marcado: Define o texto do rótulo rotulo_texto como uma string vazia ("").
    rotulo_texto.config(text="")

janela = tk.Tk()#Cria a janela principal da interface gráfica usando o módulo tkinter.
janela.title("Checkbox e Texto Oculto")#Define o título da janela como "Checkbox e Texto Oculto".

rotulo_texto = tk.Label(janela, text="")#Cria um label tkinter com o texto inicial vazio ("") e o empacota na janela principal (pack()).
rotulo_texto.pack(pady=20)#Adiciona espaço vertical de 20 pixels acima e abaixo do rótulo.

var_checkbox = tk.BooleanVar()#Cria uma variável tkinter do tipo BooleanVar para armazenar o estado do checkbox (marcado ou não marcado).
checkbox = tk.Checkbutton(janela, text="Mostrar Texto", var=var_checkbox, command=mostrar_texto)#Cria um checkbox tkinter com o texto "Mostrar Texto", associado à variável var_checkbox e que chama a função mostrar_texto() quando clicado.
checkbox.pack(pady=20)#Empacota o checkbox na janela principal com 20 pixels de espaço vertical acima e abaixo.

janela.mainloop()#Este comando inicia o loop principal da interface gráfica. O loop principal fica à espera de eventos do usuário, como cliques de mouse e pressionamentos de teclas, e atualiza a interface de acordo com esses eventos. A interface gráfica permanece aberta enquanto o loop principal estiver em execução.