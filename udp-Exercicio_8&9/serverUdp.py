import socket
import psutil

udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udpServer.bind((socket.gethostname(), 9991))

disco = psutil.disk_usage('.')
total = round(disco.total / (1024 * 1024 * 1024), 2)
available = total - round(disco.used / (1024 * 1024 * 1024), 2)


def main():
    try:

        print("Listening to the port", 9991)
        (msg, client) = udpServer.recvfrom(1024)
        if msg.decode() == 'y':
            udpServer.sendto('Espaço total : {}GB e available: {}GB'.format(total, available).encode('utf-8'), client)

        else:
            udpServer.sendto('Erro: Digite (y).'.encode('utf-8'), client)

        udpServer.close()

    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()

