import time  # Importa o módulo 'time' para usar a função 'sleep' para pausar a execução.
from datetime import datetime  # Importa a classe 'datetime' do módulo 'datetime' para trabalhar com data e hora.
from ai_gemini import send_ai # Importa a classe send_ia do módulo ai_gemini para enviar mensagens ao Google gemini.
from add_data_json import adicionar_retorno_json # Importa a classe adicionar_retorno_json do módulo add_data_json para para armesenar json recebido em um unico arquivo.
#from api_blocked import block_ip

def registrar_log(mensagem): #Cria a função regista_log
    """
    Esta função recebe uma string como mensagem e a registra em um arquivo de log 
    com um nome de arquivo baseado na data e hora atuais.
    -Adicionado chamada a funão sens_ai do arquivo ai_gemini, dessa forma permitindo a analise do log enviado
    """
    print('Função registrador_log acionada')
    dados = "dados/dados.json"
    agora = datetime.now()  # Obtém a data e hora atuais usando a classe 'datetime'.
    nome_arquivo_temp = agora.strftime("%Y%m%d%H%M") + ".log"  # Formata a data e hora no formato AAAAMMDDhhmm e adiciona ".log" para criar o nome do arquivo.
    nome_arquivo = "logs/"+nome_arquivo_temp

    try:  # Tenta executar o bloco de código a seguir. Se ocorrer um erro, o bloco 'except' será executado.
        with open(nome_arquivo, "a") as arquivo_log:  # Abre o arquivo de log no modo 'append' (adiciona ao final do arquivo). 
            arquivo_log.write(f"{mensagem}\n")  # Escreve  mensagem e uma nova linha no arquivo. 
            print("Acionando Google Gemini")
            retorno_ai = send_ai(mensagem) # Chama a função send_ai do arquivo ai_gemini.py
            print("Acionando add_data_json")
            adicionar_retorno_json(dados,retorno_ai) # Salva a informação para exebição WEB
            #block_ip(retorno_ai) # Envia para bloqueio do IP
            #print(f"Resposta do Gemini: \n{retorno_ai}")
    except Exception as e:  # Captura qualquer exceção (erro) que ocorra durante a abertura ou escrita do arquivo.
        print(f"Registrador: Erro ao registrar log: {e}")  # Exibe uma mensagem de erro no console.

