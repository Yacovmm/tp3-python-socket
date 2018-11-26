import socket
import os


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host, port = socket.gethostname(), 8881

    try:
        s.bind((host, port))
        s.listen(5)
        print("Servidor de nome %s esperando conexão na gate %s" % (host, port))

        while True:
            (client, addr) = s.accept()
            file = client.recv(1024)
            file = file.decode('utf-8')
            error = -1

            if os.path.isfile(file):

                size = os.stat(file).st_size
                client.send(str(size).encode())

                s = open(file, 'rb')
                bytes_count = s.read(4096)

                while bytes_count:
                    client.send(bytes_count)
                    bytes_count = s.read(4096)
            else:
                client.send(str(error).encode('ascii'))
                print('O arquivo não existe!')

    except Exception as error:
        print(error)
    s.close()


if __name__ == '__main__':
    main()
