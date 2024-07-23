import os

TAMANHO_CABECALHO = 4
TAMANHO_TAMREGISTRO = 2

def busca(ID_BUSCA):
    with open('dados.dat','br') as arquivo_dados:
        print(f'\n\nBusca pelo registro de chave "{ID_BUSCA}"')

        TAMANHO_ARQ = arquivo_dados.seek(0, os.SEEK_END)

        #print(f'Tamanho: {TAMANHO_ARQ}')
        
        arquivo_dados.seek(TAMANHO_CABECALHO, os.SEEK_SET)
        #print(f'Nova posição: {arquivo_dados.tell()}')

        '''
        TOTALREG = arquivo_dados.read(TAMANHO_TAMREGISTRO)
        print(TOTALREG)

        print(int.from_bytes(TOTALREG))

        arquivo_dados.seek(int.from_bytes(TOTALREG), os.SEEK_CUR)
        print(arquivo_dados.tell())

        TOTALREG = arquivo_dados.read(TAMANHO_TAMREGISTRO)
        print(TOTALREG)
        '''

        naoAchou = True
        iterador = 0

        while naoAchou == True:
            iterador += 1

            # Pega o tamanho do Registro
            TOTALREG = arquivo_dados.read(TAMANHO_TAMREGISTRO)
            #print(f'Tamanho em BYTES do registro: {TOTALREG}')
            
            # Converte o tamanho do Registro pra inteiro
            #print(f'Tamanho convertido de bytes pra INTEIRO: {int.from_bytes(TOTALREG)}')

            # Pega a posicao inicial do registro antes de ler o ID
            posicao_inicio = arquivo_dados.tell()

            registro = arquivo_dados.read(int.from_bytes(TOTALREG)).decode('utf-8')
            registro_em_lista = registro.split('|')

            # Mostra o ID do Registro
            # print(registro_em_lista[0])

            if registro_em_lista[0] == ID_BUSCA:
                print(registro, f' ({int.from_bytes(TOTALREG)} bytes)')
                naoAchou = False

            #print(arquivo_dados.tell())

            # Pula para o próximo registro (set na posição onde fica o tamanho do registro anterior e depois pula o valor em bytes)
            arquivo_dados.seek(posicao_inicio, os.SEEK_SET)
            #print(arquivo_dados.tell())
            arquivo_dados.seek(int.from_bytes(TOTALREG), os.SEEK_CUR)
            #print(f'Posição do seek depois de pular o registro {arquivo_dados.tell()}')


            if arquivo_dados.tell() >= TAMANHO_ARQ:
                naoAchou = False

            


