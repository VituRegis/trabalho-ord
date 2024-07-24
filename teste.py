import os

with open('dados copy.dat','rb+') as arq:
    arq.seek(0, os.SEEK_SET)
    cabecalho = arq.read(4)
    valor_cabecalho = int.from_bytes(cabecalho)

    arq.seek(0, os.SEEK_SET)
    print(cabecalho)
    arq.seek(0, os.SEEK_SET)
    print(valor_cabecalho)

    arq.seek(valor_cabecalho, os.SEEK_SET)
    print(arq.read(10))