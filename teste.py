import os

with open('dados copy.dat','rb+') as arq:
    arq.seek(0, os.SEEK_SET)
    cabeca_led_bytes = arq.read(4)
    cabeca_led_inteiro = int.from_bytes(cabeca_led_bytes)
    
    arq.seek(cabeca_led_inteiro, os.SEEK_SET)
    
    print(arq.read(16))

    arq.seek(cabeca_led_inteiro, os.SEEK_SET)
    tam_disponivel = int.from_bytes(arq.read(2))
    print('Tamanho registro:', tam_disponivel)

    arq.seek(2, os.SEEK_CUR)

    print(arq.read(4))
    prox_registro = int.from_bytes(arq.read(4))
    print('Localizacao prox registro:', tam_disponivel)

    arq.seek(prox_registro, os.SEEK_SET)
