'''7 - Crie um programa que percorre uma lista de números inteiros e imprime apenas os que são números primos. 
Use o for para iterar, if para a verificação e continue para pular os que não são primos.
'''

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero < 2:
        continue
    for i in range(2, numero):
        if numero % i == 0:
            continue  # não é primo, sai desse laço
            break
    else:
        print(numero)
