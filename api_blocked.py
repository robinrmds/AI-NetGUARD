import json
import requests

def api_host(remote_IP):
    # Função de emplo, deverá ser ataptada a seus dispositivos
    
    # Array de APIs
    apis = [
        {'url': 'https://api.exemplo1.com/', 'token': 'seu_token_api_1'},
        {'url': 'https://api.exemplo2.com/', 'token': 'seu_token_api_2'},
        {'url': 'https://api.exemplo3.com/', 'token': 'seu_token_api_3'}
    ]

    # IP a ser bloqueado
    ip_bloquear = remote_IP

    # Loop para enviar a requisição para cada API
    for api in apis:
        url = f"{api['url']}{api['token']}/{ip_bloquear}" 
        #resposta = requests.post(url)
        #Exemplo não funcinal, deverá ser adaptado aos seus dispotivos
        resposta = 200
        
        #if resposta.status_code == 200:
        if resposta == 200:
            print(f"Bloqueio de IP {ip_bloquear} na API {api['url']} bem-sucedido!")
        else:
           # print(f"Erro ao bloquear IP {ip_bloquear} na API {api['url']}: {resposta.status_code}")
           print(f"Erro ao bloquear IP {ip_bloquear} na API {api['url']}: 404")


def block_ip(json_data):
  """Imprime os valores da coluna 'ATACANTE' de um objeto JSON.

  Args:
      json_data: Uma string JSON ou um objeto Python representando o JSON.
  """
  try:
      if isinstance(json_data, str):
          data = json.loads(json_data)  # Converte a string JSON em um objeto Python
      else:
          data = json_data

      if isinstance(data, list):
          for item in data:
              if isinstance(item, dict) and 'ATACANTE' in item:
                 
                  api_host(item['ATACANTE'])
      elif isinstance(data, dict) and 'ATACANTE' in data:
          
          api_host(item['ATACANTE'])
      else:
          print("A coluna 'ATACANTE' não foi encontrada no JSON.")
  except json.JSONDecodeError:
      print("Erro: JSON inválido.")


