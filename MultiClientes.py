import socket
import threading
import time


def cliente_simples(flag, conteudo):
    HOST = '127.0.0.1'
    PORT = 5000
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mensagem = f"{flag}|||{conteudo}"
    cliente.sendto(mensagem.encode('utf-8'), (HOST, PORT))
    resposta, _ = cliente.recvfrom(4096)
    print(f"Resposta do servidor para flag {flag}: {resposta.decode()}")
    cliente.close()


conteudo_teste = "1\n2\n3\n4\n5"

threads = []
for i in range(1, 6):
    t = threading.Thread(
        target=cliente_simples,
        args=(str(i % 3 + 1), conteudo_teste)
    )
    threads.append(t)
    t.start()
    time.sleep(0.1)

for t in threads:
    t.join()
