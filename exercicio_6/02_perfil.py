'''2 - Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
** Instale o modulo requests - pip install requests **
URL da API que retorna um usuário aleatório no formato JSON
    url = "https://randomuser.me/api/"

'''
import requests
def gerar_usuario():
     url = "https://randomuser.me/api/"
     resposta = requests.get(url)
     if resposta.status_code == 200:
          dados = resposta.json()
          usuario = dados['results'][0]
          nome_completo = f"{usuario['name']['title']} {usuario['name']['first']} {usuario['name']['last']}"
          email = usuario['email']
          pais = usuario['location']['country']
          print("Perfil de usuário gerado.")
          print("Nome: ", nome_completo)
          print("Email: ", email)
          print("Pais: ", pais)
     else:
          print(f"Erro ao acessar a API. Código de status: {resposta.status_code}")
gerar_usuario()