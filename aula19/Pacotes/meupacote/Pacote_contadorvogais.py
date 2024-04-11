def contador_vogais(s):
    vogais = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vogais)
    print(f"O número total de vogais na string é: {count}")
    return count