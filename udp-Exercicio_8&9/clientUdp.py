import socket

clientUdp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (socket.gethostname(), 9991)


def main():
    try:

        print('Waiting the server in the port', 9991)
        ask = input("Deseja receber o espaço total(y/n):")
        clientUdp.sendto(ask.encode(), server)

        (msg, cliente) = clientUdp.recvfrom(1024)
        print(msg.decode('utf-8'))

        clientUdp.close()

    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
