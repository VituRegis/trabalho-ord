import os

arquivo_dados = open('dados.dat','br+')

def buscaEspacoNaLED(tam_registro):
    lista_registros_tam = []

    arquivo_dados.seek(0, os.SEEK_SET)
    cabeca_led_bytes = arquivo_dados.read(4)
    cabeca_led_inteiro = int.from_bytes(cabeca_led_bytes)
    
    arquivo_dados.seek(cabeca_led_inteiro, os.SEEK_SET)
    
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

    melhor_loc = 0
    melhor_tam = 0
    melhor_i = 0
    i = 0

    for loc, tam  in lista_registros_tam:
        if tam >= tam_registro and tam >= melhor_tam and tam != 0: 
            melhor_tam = tam
            melhor_loc = loc
            melhor_i   = i
        
        i += 1

    anterior_loc = 0
    anterior_tam = 0
    posterior_loc = 0
    posterior_tam = 0

    for j, registro in enumerate(lista_registros_tam):
        if j == melhor_i - 1:
            anterior_loc = registro[0]
            anterior_tam = registro[1]
        if j == melhor_i + 1:
            posterior_loc = registro[0]
            posterior_tam = registro[1]

    return melhor_tam, melhor_loc, anterior_tam, anterior_loc, posterior_tam, posterior_loc if melhor_tam > 0 else arquivo_dados.seek(0, os.SEEK_END)

def insere(registro):
    lista_registro = registro.split('|')
    print(f'\nInserção do registro de chave "{lista_registro[0]}" ({len(registro)} bytes)')

    tamanho_escolhido, offset_escolhido, tamanho_anterior, offset_anterior, tamanho_posterior, offset_posterior = buscaEspacoNaLED(len(registro))
    tamanho_sobra = tamanho_escolhido - len(registro)
    eh_final = False

    #print('\n',tamanho_escolhido, offset_escolhido, tamanho_anterior, offset_anterior, tamanho_posterior, offset_posterior , sep='\n')
    
    if tamanho_anterior != 0 and tamanho_posterior != 0: # TA NO MEIO DA LED
        if tamanho_sobra < 16:
            arquivo_dados.seek(offset_escolhido, os.SEEK_SET)
            arquivo_dados.seek(2, os.SEEK_CUR) 
            arquivo_dados.write(registro.encode('utf-8'))
            for i in range(tamanho_sobra):
                arquivo_dados.write(' '.encode('utf-8')) 

            arquivo_dados.seek(offset_anterior,os.SEEK_SET)
            arquivo_dados.seek(4,os.SEEK_CUR)
            arquivo_dados.write(offset_posterior.to_bytes(4, byteorder='big'))
        else:
            arquivo_dados.seek(offset_escolhido, os.SEEK_SET)
            arquivo_dados.write(len(registro).to_bytes(2, byteorder='big'))
            arquivo_dados.write(registro.encode('utf-8'))

            offset_sobra = arquivo_dados.tell()
            arquivo_dados.write(tamanho_sobra.to_bytes(2, byteorder='big'))
            arquivo_dados.write('*|'.encode('utf-8'))
            arquivo_dados.write(offset_posterior.to_bytes(4, byteorder='big'))            
    elif tamanho_anterior == 0 and tamanho_posterior != 0: # SIGNIFICA QUE É O PRIMEIRO DA LED
        if tamanho_sobra < 16:
            arquivo_dados.seek(offset_escolhido, os.SEEK_SET)
            arquivo_dados.seek(2, os.SEEK_CUR) 
            arquivo_dados.write(registro.encode('utf-8'))
            for i in range(tamanho_sobra):
                arquivo_dados.write(' '.encode('utf-8')) 

            arquivo_dados.seek(0, os.SEEK_SET)
            arquivo_dados.write(offset_posterior.to_bytes(4, byteorder='big'))
        else:
            arquivo_dados.seek(offset_escolhido, os.SEEK_SET)
            arquivo_dados.write(len(registro).to_bytes(2, byteorder='big'))
            arquivo_dados.write(registro.encode('utf-8'))

            offset_sobra = arquivo_dados.tell()
            arquivo_dados.write(tamanho_sobra.to_bytes(2, byteorder='big'))
            arquivo_dados.write('*|'.encode('utf-8'))

            arquivo_dados.seek(0, os.SEEK_SET)
            arquivo_dados.write(offset_posterior.to_bytes(4, byteorder='big'))
    elif tamanho_anterior != 0 and tamanho_posterior == 0: # SIGNIFICA QUE É O ÚLTIMO DA LED
        if tamanho_sobra < 16:
            arquivo_dados.seek(offset_escolhido, os.SEEK_SET)
            arquivo_dados.seek(2, os.SEEK_CUR) 
            arquivo_dados.write(registro.encode('utf-8'))
            for i in range(tamanho_sobra):
                arquivo_dados.write(' '.encode('utf-8')) 
        else:
            arquivo_dados.seek(offset_escolhido, os.SEEK_SET)
            arquivo_dados.write(len(registro).to_bytes(2, byteorder='big'))
            arquivo_dados.write(registro.encode('utf-8'))

            arquivo_dados.write(tamanho_sobra.to_bytes(2, byteorder='big'))
            arquivo_dados.write('*|'.encode('utf-8'))

            arquivo_dados.seek(0, os.SEEK_SET)
            arquivo_dados.write(tamanho_sobra.to_bytes(4, byteorder='big'))
    elif tamanho_anterior == 0 and tamanho_posterior == 0 and tamanho_escolhido != 0: # EH O PRIMEIRO E O ULTIMO VULGO PRIMEIRO REGISTRO
        if tamanho_sobra < 16:
            arquivo_dados.seek(offset_escolhido, os.SEEK_SET)
            arquivo_dados.seek(2, os.SEEK_CUR) 
            arquivo_dados.write(registro.encode('utf-8'))
            for i in range(tamanho_sobra):
                arquivo_dados.write(' '.encode('utf-8')) 

            arquivo_dados.seek(0, os.SEEK_SET)
            arquivo_dados.write(int(0).to_bytes(4, byteorder='big'))
        else:
            arquivo_dados.seek(offset_escolhido, os.SEEK_SET)
            arquivo_dados.write(len(registro).to_bytes(2, byteorder='big'))
            arquivo_dados.write(registro.encode('utf-8'))

            offset_sobra = arquivo_dados.tell()
            arquivo_dados.write(tamanho_sobra.to_bytes(2, byteorder='big'))
            arquivo_dados.write('*|'.encode('utf-8'))

            arquivo_dados.seek(0, os.SEEK_SET)
            arquivo_dados.write(offset_sobra.to_bytes(4, byteorder='big'))
    else: # EH O VAI PRO FINAL
        arquivo_dados.seek(0, os.SEEK_END)
        arquivo_dados.write(len(registro).to_bytes(2, byteorder='big'))
        arquivo_dados.write(registro.encode('utf-8'))

        eh_final = True

    if eh_final:
        print('Local: fim do arquivo!')
    elif tamanho_sobra > 16:
        print(f'Tamanho do espaço reutilizado: {tamanho_escolhido} bytes (Sobra de {tamanho_escolhido - len(registro) - 2} bytes)')
        print(f'Local: offset = {offset_escolhido} bytes ({hex(offset_escolhido)})')
    else:    
        print(f'Tamanho do espaço reutilizado: {tamanho_escolhido - 2} bytes')
        print(f'Local: offset = {offset_escolhido} bytes ({hex(offset_escolhido)})')