import json
from api_blocked import block_ip

def format_to_json(string_json):
    # Remove as marcas ```json e espaços em branco no início e fim
    indice_colchete_abre = string_json.find('[')
    string_json = string_json[indice_colchete_abre:].strip()
    indice_colchete_fecha = string_json.rfind(']')
    string_json = string_json[:indice_colchete_fecha+1].strip()

    string_json = string_json.replace("\n", "").replace("}, {", "}, {")
    return string_json


def adicionar_retorno_json(arquivo_json, novo_retorno):
    """Adiciona um novo retorno a um arquivo JSON existente.

    Args:
        arquivo_json: Caminho para o arquivo JSON existente.
        novo_retorno: Dicionário contendo o novo retorno a ser adicionado.
    """
    novo_retorno = format_to_json(novo_retorno)
    print("Acionado add_data_json")
    try:
        with open(arquivo_json, 'r+') as f:
            data = json.load(f)
            # Verifica se os dados carregados são uma lista. Se não for,
            # assume que é um dicionário e o envolve em uma lista para que 
            # possamos adicionar o novo retorno.
            if not isinstance(data, list):
                data = [data]
            novo_retorno = novo_retorno.replace('\\', '').encode().decode('unicode-escape')
            dados = json.loads(novo_retorno)
            block_ip(dados) # Envia para bloqueio do IP
            data.append(dados)
            f.seek(0)  # Move o cursor para o início do arquivo
            json.dump(data, f, indent=4)  # Sobrescreve o arquivo com os dados atualizados

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo_json}")
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON em {arquivo_json}. Verifique se o arquivo está formatado corretamente.")

# Exemplo de uso:
# adicionar_retorno_json("arquivo.json", "{\"chave\": \"valor\"}")
