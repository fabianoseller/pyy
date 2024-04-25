# Criando o dicionário de números de telefone para nomes de pessoas
agenda = {
    "123456789": "João Silva",
    "987654321": "Maria Oliveira",
    "456789012": "Ana Souza",
}

# Definindo o número de telefone a ser removido
numero_a_remover = "987654321"

# Removendo o número de telefone do dicionário
numero_removido = agenda.pop(numero_a_remover)

# Verificando se a chave foi removida
if numero_a_remover in agenda:
    print(f"O número de telefone '{numero_a_remover}' ainda está na agenda.")
else:
    print(f"O número de telefone '{numero_removido}' foi removido com sucesso.")