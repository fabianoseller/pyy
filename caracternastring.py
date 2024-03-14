# /*Verificar se um caractere está presente em uma string:
# Escrever um programa que verifica se um caractere digitado pelo usuário está
# presente em uma string e informa o resultado.*/


# Módulo RegEx
# Python tem um pacote embutido chamado , que pode ser usado para trabalhar com Expressões regulares.re

# Importe o módulo:re

import re

#Retorna a lista de conteudo: "in":

txt = "Flores são como pontos de luz na paisagem da vida. Na inglaterra, Elas desabrocham com delicadeza, inundando o mundo com cores e fragrâncias. Inspiram poetas, encantam amantes e alegram os corações. Incluo aqui meu pequeno tributo: “Em um jardim infinito, as flores dançam ao vento, inspirando sonhos e invocando a primavera"
x = re.findall("in", txt)
print(x)
