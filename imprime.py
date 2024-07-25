import os

arquivo_dados = open('dados.dat','br+')

def imprime():
    lista_registros_tam = []

    arquivo_dados.seek(0, os.SEEK_SET)
    cabeca_led_bytes = arquivo_dados.read(4)
    cabeca_led_inteiro = int.from_bytes(cabeca_led_bytes)
    
    arquivo_dados.seek(cabeca_led_inteiro, os.SEEK_SET)
    tam_disponivel = int.from_bytes(arquivo_dados.read(2))

    lista_registros_tam.append([cabeca_led_inteiro, tam_disponivel])

    iterador = 0

    while tam_disponivel > 0:
        iterador += 1

        arquivo_dados.seek(2, os.SEEK_CUR)

        prox_registro = int.from_bytes(arquivo_dados.read(4))

        arquivo_dados.seek(prox_registro, os.SEEK_SET)
        tam_disponivel = int.from_bytes(arquivo_dados.read(2))

        lista_registros_tam.append([prox_registro, tam_disponivel])

    print('LED ->', end=' ')

    for loc, tam  in lista_registros_tam:
        if tam != 0:
            print(f'[offset: {loc}, tam: {tam}] ->', end=' ')

    
    print('[FIM]')
        