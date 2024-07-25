import os

arquivo_dados = open('dados copy.dat','br+')

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
        #print('Localizacao prox registro:', prox_registro)
        arquivo_dados.seek(prox_registro, os.SEEK_SET)
        tam_disponivel = int.from_bytes(arquivo_dados.read(2))
        #print(f'Tamanho registro {iterador}:', tam_disponivel)

        lista_registros_tam.append([prox_registro, tam_disponivel])

    print(lista_registros_tam)

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
        if melhor_i < i and  melhor_i > 0 and j == melhor_i - 1:
            anterior_loc = registro[0]
            anterior_tam = registro[1]
            #print('ANTERIOR AO MELHOR: ', registro[0], registro[1])
        if melhor_i < i and j == melhor_i + 1:
            posterior_loc = registro[0]
            posterior_tam = registro[1]
            #print('POSTERIOR AO MELHOR: ', registro[0], registro[1])

            


    return melhor_tam, melhor_loc, anterior_tam, anterior_loc, posterior_tam, posterior_loc if melhor_tam > 0 else arquivo_dados.seek(0, os.SEEK_END)

def insere(registro):
    tamanho_escolhido, offset_escolhido, tamanho_anterior, offset_anterior, tamanho_posterior, offset_posterior = buscaEspacoNaLED(len(registro))
    tamanho_sobra = tamanho_escolhido - len(registro)
    print('Sobra: ', tamanho_sobra)


    if tamanho_anterior != 0 and tamanho_posterior != 0: # TA NO MEIO DA LED
        print('O CERTO EH PASSAR NESSE AQUI')
        ...
        # QUANDO TA NO MEIO DA LED PRECISA SUBSTITUIR E DEPOIS
        # SE TIVER SOBRA ELA DEVE APONTAR PRO POSTERIOR
        # SE NAO TIVER SOBRA O ANTERIOR DEVE APONTAR PRO POSTERIOR
        # SE A SOBRA FOR MENOR QUE 16 SUBSTITUIR OS BYTES RESTANTES POR .
    elif tamanho_anterior == 0: # SIGNIFICA QUE É O PRIMEIRO DA LED
        
        ... 
        # SUBSTITUIR E CASO HAJA SOBRA A SOBRA VIRA A PRIMEIRA DA LED
        # SE NAO HOUVER SOBRA O OFFSET_POSTERIOR VIRA O PROXIMO
        # SE A SOBRA FOR MENOR QUE 16 SUBSTITUIR OS BYTES RESTANTES POR .
    elif tamanho_posterior == 0: # SIGNIFICA QUE É O ÚLTIMO DA LED
            # ABAIXO AQUI TA ERRADO PQ TEM Q VERIFICAR A SOBRA ANTES DE COMEÇAR A PREENCHER

        #arquivo_dados.seek(offset_escolhido, os.SEEK_SET)
        #arquivo_dados.write(len(registro).to_bytes(4, byteorder='big'))
        #arquivo_dados.write(registro.encode('utf-8'))

        #if tamanho_sobra > 16:
        #    for i in range(tamanho_sobra):
        #        arquivo_dados.write()
        #else:


        # SUBSTITUIR E CASO HAJA SOBRA A SOBRA PRECISA APONTAR O ANTERIOR PRA SOBRA
        # SE NAO HOUVER SOBRA SOMENTE SUBSTITUIR OS BYTES RESTANTES POR .

    #print('ANTERIOR AO MELHOR: ', offset_anterior , 'tam: ', tamanho_anterior)
    #print('POSTERIOR AO MELHOR: ', offset_posterior, 'tam: ', tamanho_posterior)
    #print(f'\nTamanho escolhido: {tamanho_escolhido} \nByteOffset: {offset_escolhido}')

insere('144|The Sims|2000|Life simulation|Electronic Arts|PC|')