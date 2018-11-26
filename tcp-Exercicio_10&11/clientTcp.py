import socket
import pickle
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = socket.gethostname(), 8881


def main():
    s.connect((host, port))

    file = "arquivo.txt"
    s.send(file.encode('utf-8'))

    msg = s.recv(8)

    size = int(msg.decode())

    if size >= 0:

        print(f"Tamanho do arquivo {size}")

        if os.path.isdir('files') is not True:
            os.mkdir('files')

        file = open('files/' + file, 'wb')
        bytes_count = s.recv(4096)

        count = 0

        while bytes_count:
            file.write(bytes_count)
            count += len(bytes_count)
            loading(count, size)
            if count == size:
                break
            bytes_count = s.recv(4096)
        print("Done")

    else:
        print("Arquivo não encontrado!")

    s.close()


def loading(bytes, size):
    kbytes = bytes / 1024
    tam_bytes = size / 1024
    txt = 'Baixando... '
    txt += '{:<.2f}'.format(kbytes) + ' KB '
    txt += 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(txt)

if __name__ == '__main__':
    main()
