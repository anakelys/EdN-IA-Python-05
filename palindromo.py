def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto == texto[::-1]

palavra = input("Digite uma palavra ou frase: ")

if eh_palindromo(palavra):
    print("Sim, é palíndromo")
else:
    print("Não, não é palíndromo")
