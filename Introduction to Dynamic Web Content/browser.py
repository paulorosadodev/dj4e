import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 'socket.AF_INET' especifica que estamos usando IPv4 como o protocolo de endereço. // 'socket.SOCK_STREAM' especifica que estamos usando TCP como o protocolo de transporte.

mysock.connect(('data.pr4e.org', 80)) # Estabelece uma conexão com o host remoto 'data.pr4e.org' na porta '80'

cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() # Cria uma solicitação HTTP GET que será enviada ao servidor. A string 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n' é a mensagem HTTP que será enviada para o servidor. O método '.encode()' é usado para converter a string em bytes, pois os dados enviados através do socket precisam ser bytes em Python 3.

mysock.send(cmd) # Envia a solicitação HTTP para o servidor usando o método 'send()' do objeto de soquete mysock. A solicitação GET é enviada para o servidor para obter o conteúdo da página 'page1.htm'.

while True:
    data = mysock.recv(512) # Recebe até 512 bytes de dados do servidor e os armazena na variável data.
    if len(data) < 1: # Verifica se não há mais dados a serem recebidos do servidor. Se o comprimento dos dados recebidos for menor que 1, isso significa que a transmissão de dados do servidor foi concluída.
        break
    print(data.decode(), end='') # Decodifica os dados recebidos de bytes para uma string usando o método '.decode()' e imprime esses dados na tela. O parâmetro "end=''" é usado para garantir que a impressão não adicione uma nova linha.

mysock.close() # Fecha o socket, encerrando a conexão com o servidor. Isso é feito usando o método close() do objeto de soquete mysock.