import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((HOST, PORT))

print(f"Servidor UDP iniciado em {HOST}:{PORT}")


def tratar_cliente(dados, endereco):
    mensagem = dados.decode('utf-8')
    try:
        flag, conteudo = mensagem.split('|||', 1)
        numeros = [
            float(linha)
            for linha in conteudo.strip().split('\n')
            if linha.strip()
        ]
    except Exception:
        resposta = "Erro: arquivo vazio ou formato inválido."
        servidor.sendto(resposta.encode('utf-8'), endereco)
        return

    if flag == '1':
        resposta = f"soma: {sum(numeros)}"
    elif flag == '2':
        resposta = f"media: {sum(numeros) / len(numeros)}"
    elif flag == '3':
        resposta = f"maior: {max(numeros)} e o menor: {min(numeros)}"
    elif flag == '4':
        resposta = "Encerrando o servidor."
        servidor.sendto(resposta.encode('utf-8'), endereco)
        print("Servidor encerrado pelo cliente.")
        servidor.close()
        exit(0)
    else:
        resposta = "flag invalida"

    servidor.sendto(resposta.encode('utf-8'), endereco)


while True:
    dados, endereco = servidor.recvfrom(4096)
    thread = threading.Thread(target=tratar_cliente, args=(dados, endereco))
    thread.start()
