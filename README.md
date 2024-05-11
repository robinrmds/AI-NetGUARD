
# AI-NetGUARD:  Proteção Inteligente Contra Ataques Cibernéticos 
Em um mundo cada vez mais conectado, a segurança digital se torna uma necessidade fundamental. É nesse cenário que surge o AI-NetGUARD, um software inovador que utiliza a inteligência artificial do Google Gemini para proteger seus dispositivos e aplicações contra ataques cibernéticos, além de automatizar a resposta a ameaças.
O AI-NetGUARD opera de maneira inteligente e proativa. Ele funciona analisando os logs enviados ao servidor syslog, que registra eventos e atividades relevantes em sua rede. Esses logs são então submetidos à poderosa IA do Gemini, que realiza uma avaliação minuciosa para determinar se o log representa um risco potencial de ataque.
Veja como funciona:
1.	Coleta de dados: O AI-NetGUARD coleta logs de diferentes fontes, como servidores, firewalls, roteadores e outros dispositivos de rede, centralizando as informações no servidor syslog.
2.	Análise inteligente: A IA do Gemini entra em ação, utilizando algoritmos avançados para analisar os logs em busca de padrões suspeitos, anomalias e indicadores de possíveis ataques.
3.	Identificação de ameaças: O Gemini, com sua capacidade de aprendizado de máquina, identifica potenciais ameaças com alta precisão, reconhecendo desde ataques de força bruta até atividades mais sofisticadas, como malware e phishing.
4.	Alertas e respostas: O AI-NetGUARD gera alertas em tempo real sobre as ameaças detectadas, permitindo que os administradores de rede tomem medidas preventivas e corretivas rapidamente. Além disso, o sistema pode ser configurado para acionar automaticamente APIs de firewall ou outros sistemas de segurança para bloquear IPs de atacantes, neutralizando a ameaça de forma rápida e eficiente.
Benefícios do AI-NetGUARD:
•	Proteção proativa: Detecção precoce de ameaças, antes que causem danos reais.
•	Análise precisa: A IA do Gemini garante a identificação eficiente de atividades maliciosas.
•	Resposta rápida e automatizada: Bloqueio automático de IPs de atacantes através de APIs, além de alertas em tempo real que permitem ações imediatas para neutralizar as ameaças.
•	Eficiência aprimorada: Automatiza a análise de logs e a resposta a ameaças, liberando tempo para outras tarefas.
•	Adaptabilidade: O sistema aprende com os dados e se adapta às novas ameaças.
O AI-NetGUARD representa um avanço significativo na segurança digital, oferecendo uma solução inteligente e eficaz para proteger seus dados e sistemas. Com sua combinação de análise de logs, inteligência artificial e automação de resposta, o AI-NetGUARD se torna uma ferramenta essencial para garantir a segurança da sua rede.

# Instruções de instalação
•	Instalar o Python em seu sistema operacional </br>
•	Instalar a biblioteca do Google Gemini</br>
->	pip install google-generativeai</br>
•	Instalar a biblioteca do Flask</br>
o	pip install -U Flask</br>
# Executando o AI-NetGUARD
•	Windows - PowerShell</br>
   python .\main.py</br>
•	Linux - Bash</br>
   python  ./main.py</br>

# Acesso WEB
http://127.0.0.1:5000
