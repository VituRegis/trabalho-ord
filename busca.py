import os

TAMANHO_CABECALHO = 4
TAMANHO_TAMREGISTRO = 2

def busca(ID_BUSCA):
    with open('dados.dat','br') as arquivo_dados:
        print(f'\n\nBusca pelo registro de chave "{ID_BUSCA}"')

        TAMANHO_ARQ = arquivo_dados.seek(0, os.SEEK_END)
        
        arquivo_dados.seek(TAMANHO_CABECALHO, os.SEEK_SET)

        naoAchou = True
        iterador = 0

        while naoAchou == True:
            iterador += 1

            # Pega o tamanho do Registro
            TOTALREG = arquivo_dados.read(TAMANHO_TAMREGISTRO)

            # Pega a posicao inicial do registro antes de ler o ID
            posicao_inicio = arquivo_dados.tell()
            
            registro_bytes = arquivo_dados.read(int.from_bytes(TOTALREG))
            try:
                registro = registro_bytes.decode('utf-8')
                registro_em_lista = registro.split('|')

                if registro_em_lista[0] == ID_BUSCA:
                    print(registro, f' ({int.from_bytes(TOTALREG)} bytes)')
                    naoAchou = False
                    break
            except UnicodeDecodeError:
                ...

            # Pula para o próximo registro (set na posição onde fica o tamanho do registro anterior e depois pula o valor em bytes)
            arquivo_dados.seek(posicao_inicio, os.SEEK_SET)
            arquivo_dados.seek(int.from_bytes(TOTALREG, byteorder='big'), os.SEEK_CUR)


            if arquivo_dados.tell() >= TAMANHO_ARQ:
                print('Erro: registro não encontrado!')
                naoAchou = False


