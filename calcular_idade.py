def idade_em_dias(ano_nascimento):
    ano_atual = 2025
    idade = ano_atual - ano_nascimento
    dias = idade * 365
    return dias

ano = int(input("Digite seu ano de nascimento: "))
resultado = idade_em_dias(ano)
print(f"Sua idade em dias é aproximadamente {resultado} dias.")
