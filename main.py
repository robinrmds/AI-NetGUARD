import subprocess

# Nome do arquivo Python que você deseja executar
syslog_server = "syslog_server.py"
web_site = "index.py"

# Realizando a chamado para o SyslogServer
print('Carregando Syslog Server')

# Executa o arquivo Python como um subprocesso
processo_syslog = subprocess.Popen(["python", syslog_server])  
processo_web = subprocess.Popen(["python", web_site])

