#https://blog.finxter.com/fixed-modulenotfounderror-no-module-named-tiktoken/
# pip install tiktoken

#https://pypi.org/project/tiktoken/
# 💡 If you have Windows and you have set up the py alias
# py -m pip install tiktoken

import tiktoken

string = """Herança na Programação Orientada a Objetos (POO):
A herança em POO é um conceito fundamental que permite que uma classe (chamada de classe derivada ou subclasse) herde características e comportamentos de outra classe (chamada de classe base, superclasse ou pai). Isso significa que a classe derivada pode acessar e reutilizar os membros (atributos e métodos) da classe base, além de poder adicionar novos membros ou redefinir os membros existentes, conforme necessário.
Vantagens da Herança:
Reutilização de código: Evita a redundância de código, permitindo que as classes compartilhem funcionalidades comuns da classe base.
Facilidade de Manutenção: Mudanças feitas na classe base refletem automaticamente nas classes derivadas, evitando a necessidade de alterações repetitivas em várias partes do código.
Abstração e Generalização: Permite modelar hierarquias de classes que refletem relações do mundo real, permitindo uma melhor organização e compreensão do sistema.

Herança e Estruturas de Dados: A herança é um conceito fundamental na POO que permite a criação de hierarquias de classes, enquanto as estruturas de dados são ferramentas utilizadas para organizar e gerenciar dados em um programa. A herança pode ser aplicada em conjunto com as estruturas de dados para modelar e organizar classes que representam diferentes tipos de dados e comportamentos.
Herança e Listas: As listas podem ser representadas como classes em POO, onde a herança pode ser usada para definir diferentes tipos de listas com comportamentos específicos. Por exemplo, pode-se ter uma classe base "Lista" e classes derivadas como "ListaEstática" e "ListaDinâmica", onde cada uma implementa suas próprias operações de inserção, exclusão, busca, etc. A herança facilita a reutilização de código comum a todas as implementações de listas.
Em resumo, a herança é um dos pilares da POO, permitindo a criação de hierarquias de classes que refletem relações do mundo real e proporcionam reutilização de código e abstração. As listas, por sua vez, são estruturas de dados fundamentais que podem ser implementadas usando tanto abordagens estáticas quanto dinâmicas, sendo a herança uma ferramenta valiosa para organizar e modelar diferentes tipos de listas em programas orientados a objetos."""

enc = tiktoken.encoding_for_model("gpt-4")
result = enc.encode(string)
print(len(result))

#https://saurabhjadhavblogs.com/installing-langchain-how-to-install-langchain-and-get-started-with-it
#https://python.langchain.com/docs/get_started/quickstart/