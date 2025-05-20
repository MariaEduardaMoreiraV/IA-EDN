'''1 - Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, 
possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.
'''
import random #importando o módulo RANDOM
import string #importando o módulo de caracteres prontos 

tamanho = int(input("Informe o tamanho de caracteres para gerar a senha: "))
'''Bloco para definir caracteres que serão usados.
ascii: trazendo letras maiúculas e minúsculas.
digits: trazendo números de 0 a 9.
punctuation: trazendo caracteres especiais.'''
caracteres_possives = string.ascii_letters + string.digits + string.punctuation
'''Bloco para gerar senha
random.choices: escolhe tamanho dos  elementos na lista.
'''
senha_lista = random.choices(caracteres_possives, k=tamanho)
senha = "".join(senha_lista) #aqui esta unindo os caracteres.
print("Senha gerada: ", senha)