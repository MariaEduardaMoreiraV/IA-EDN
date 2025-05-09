'''4 - Crie uma função em Python que receba um número como parâmetro e retorne o dobro desse número. Depois, chame essa função com um número fornecido pelo usuário.
'''

# Função que retorna o dobro de um número
def dobro(numero):
    return numero * 2

# Solicitar um número ao usuário
num = int(input("Digite um número: "))

# Chamar a função e exibir o resultado
resultado = dobro(num)
print(f"O dobro de {num} é {resultado}")