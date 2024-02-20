from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM) # Cria um objeto de socket (serversocket) usando a família de endereços AF_INET (IPv4) e o tipo de socket SOCK_STREAM (TCP).

    try :
        serversocket.bind(('localhost',9000)) # Associa o socket serversocket ao endereço 'localhost' e à porta 9000.

        serversocket.listen(5) # Coloca o socket em modo de escuta, permitindo que ele aceite conexões de entrada. O argumento '5' especifica o tamanho da fila de conexões pendentes.

        while(1):
            (clientsocket, address) = serversocket.accept() # Aceita uma conexão de um cliente. O método 'accept()' retorna uma tupla contendo um novo socket (clientsocket) para comunicação com o cliente e o endereço (address) do cliente.

            rd = clientsocket.recv(5000).decode() # Recebe dados da conexão do cliente. Aqui, estamos recebendo até 5000 bytes de dados e decodificando esses bytes em uma string.

            pieces = rd.split("\n") # Separa a string recebida em linhas
            if ( len(pieces) > 0 ) : print(pieces[0]) # imprime a primeira linha, que geralmente contém a solicitação HTTP do cliente.

            data = "HTTP/1.1 200 OK\r\n" # Prepara a resposta HTTP, definindo o cabeçalho de status como '200 OK'
            data += "Content-Type: text/html; charset=utf-8\r\n" # Especifica o tipo de conteúdo como 'text/html'
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n" # Adiciona a mensagem HTML "Hello World".

            clientsocket.sendall(data.encode()) # Envia a resposta ao cliente, convertendo a string em bytes e utilizando o método sendall() para garantir que todos os dados sejam enviados.

            clientsocket.shutdown(SHUT_WR) # Desliga a parte de escrita do socket do cliente, indicando que a resposta foi completamente enviada.

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close() # Fecha o socket do servidor após a execução do loop, liberando os recursos associados a ele.

print('Access http://localhost:9000')
createServer()
