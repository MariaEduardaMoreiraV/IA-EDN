'''2 - Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.
'''
quantidade_pares = 0
quantidade_impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'Fim' para encerrar: )")
    if entrada.lower() == 'Fim':
        break
    try:
        numero = int(numero)
        if numero % 2 == 0:
            print("O número é PAR.")
            quantidade_pares += 1
        else:
            print("O número  é ÍMPAR.")
            quantidade_impares += 1
    except ValueError:
        print("Voce deve digitar um nímero inteiro ou 'FIM'.")

print(f"Quantidade de números PARES: {quantidade_pares}")
print(f"Quantidade de números PARES: {quantidade_impares}")