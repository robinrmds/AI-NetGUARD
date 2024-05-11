import socketserver  # Importa o módulo necessário para criar um servidor de soquete UDP.

from registrador_log import registrar_log # Importa a função do arquivo registrador_log

print('->Syslog Server, listando em 127.0.0.1:514\nAguardando mensagem...')

class SyslogUDPHandler(socketserver.BaseRequestHandler):  # Define uma classe para lidar com as solicitações syslog.
    """
    Esta classe lida com cada mensagem syslog recebida.
    """
    def handle(self):
        """
        Este método é chamado para cada mensagem syslog recebida.
        """
        data = bytes.decode(self.request[0].strip())  # Decodifica os dados brutos da mensagem (bytes) para uma string.
        socket = self.request[1]  # Obtém o objeto do soquete (não utilizado neste exemplo).
        print(f"Mensagem recebida: {data}")  # Exibe a mensagem recebida no console.
        
        print('Acionando função registrador_log')
        registrar_log(data)
        # Aqui você pode processar a mensagem 'data', como armazená-la em uma variável, 
        # enviá-la para um banco de dados, etc.

if __name__ == "__main__":  # Executa o código a seguir apenas quando o script é executado diretamente.
    """
    Configura e inicia o servidor UDP para receber mensagens syslog.
    """
    HOST, PORT = "localhost", 514  # Define o host e a porta para o servidor (porta 514 é o padrão para syslog).
    with socketserver.UDPServer((HOST, PORT), SyslogUDPHandler) as server:  # Cria um servidor UDP 
        # e o associa à classe SyslogUDPHandler para processar as solicitações.
        server.serve_forever()  # Inicia o servidor e o mantém em execução para receber mensagens syslog.