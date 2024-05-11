"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

def send_ai(mensagem):
  print("Google Gemini acionado")
  genai.configure(api_key="Sua_Chave_Aqui")

  # Set up the model
  generation_config = {
    "temperature": 0.15,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
  }

  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_NONE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_NONE"
    },
  ]

  #system_instruction = "-Analisar logs de serviços  e equipamentos de rede e informar se são tentativas de ataque ou erro critico\n-a Resposta deverá ser no formato JSON, sem adição de nehum caractere\n-Em caso de erro critico:\n      - Primeira coluna:  data e hora contida no log;\n      - Segunda coluna: a ação a ser tomada, nesse caso utilizar a palavra ALERTA;\n      - Terceira coluna : IP ou hostname do equipamento ou servidor afetado;\n      - Quarta coluna: erro descrito no log\n      - Quinta coluna: sugestão de como resolver o problema\n-Em caso de ataque: O retorno da analise deverá ser no formato de uma lista Python, as colunas devem conter as seguintes informações: \n      - Primeira coluna: data e hora contida no log ;\n      - Segunda coluna:  -Segunda coluna: a ação a ser tomada, nesse caso utilizar a palavra BLOQUEAR;\n      - Terceira coluna: IP do atacante;\n      - Quarta coluna:, informar o IP ou hostname do servidor que está sendo atacado;\n      - Quinta coluna: identificação do tipo de ataque realizado com uma explicação resumida;\n "

  system_instruction = "-Analisar logs de serviços e equipamentos de rede e informar se são tentativas de ataque ou erro critico;\n-remover caracteres acentuados\n-Em caso de erro critico: O retorno da analise deverá ser no formato JSON com 5 colunas:\n    -Coluna 1 (DATA_TIME): Data e hora contida no log;\n    -Coluna 2 (ACAO): Ação a ser tomada, nesse caso utilizar a palavra ALERTA;\n    -Coluna 3 (IP_HOSTNAME): IP ou hostname do equipamento ou servidor afetado;\n    -Coluna 4 (ERRO): Erro descrito no log;\n    -Coluna 5 (SUGESTAO): Sugestão de como resolver o problema;\n    \n-Em caso de ataque: O retorno da analise deverá ser no formato JSON de 5 conulas:\n    -Coluna 1 (DATA_TIME): Data e hora contida no log;\n    -Coluna 2 (ACAO): Acao a ser tomada, nesse caso utilizar a palavra BLOQUEAR;\n    -Coluna 3 (ATACANTE): IP do atacante;\n    -Coluna 4 (IP_HOSTNAME): IP ou hostname do servidor que está sendo atacado;\n    -Coluna 5 (TIPO_ATAQUE): Identificação do tipo de ataque realizado com uma explicação resumida;"
  
    

  
  model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                generation_config=generation_config,
                                system_instruction=system_instruction,
                                safety_settings=safety_settings)

  convo = model.start_chat(history=[
  ])


  convo.send_message(mensagem)
  print("Resposta do Google Gemini:impressao desabilitada\n")
  #print(convo.last.text)
  return convo.last.text

#message = "Oct  2 06:25:46 host-vps sshd[8463]: Failed password for root from 116.31.116.17 port 31142 ssh2"
#
# send_ai(message)