import socket

HOST = '127.0.0.1'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    nomeFile = input("nome do arquivo:")
    arquivo = nomeFile
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # se o arquivo for maior que 1kb encerra
    if len(conteudo.encode('utf-8')) > 1024:
        print("Erro: O arquivo excede 1KB.")
        exit()
    # opcoes de resposta
    print("1- Soma dos numeros")
    print("2- media dos numeros")
    print("3- Maior e menor numero")
    print("4- encerrar")
    flag = input("Qual das opcoes voce escolhe? ")
    mensagem = f"{flag}|||{conteudo}"
    cliente.sendto(mensagem.encode('utf-8'), (HOST, PORT))
    resposta = cliente.recv(4096)
    print("Servidor: ", resposta.decode('utf-8'))
    if resposta.decode('utf-8') == "Encerrando o servidor.":
        cliente.close()
        break

cliente.close()
