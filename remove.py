import os

TAMANHO_CABECALHO = 4
TAMANHO_TAMREGISTRO = 2

arquivo_dados = open('dados copy.dat','br+')

def insereNoCabecalho(offset, tamanho):
    arquivo_dados.seek(0, os.SEEK_SET)
    cabecalho = arquivo_dados.read(4)
    cabecalho_inteiro = int.from_bytes(cabecalho)
    print(cabecalho_inteiro)

    if cabecalho_inteiro == 4294967295:
        arquivo_dados.seek(0, os.SEEK_SET)
        arquivo_dados.write(offset)
    else:
        arquivo_dados.seek(cabecalho_inteiro, os.SEEK_SET)
        print(arquivo_dados.read(4))
        print(arquivo_dados.tell())

        arquivo_dados.seek(0, os.SEEK_SET)
        arquivo_dados.write(offset)

    
    
    
def remove(ID_REMOCAO):
    print(f'\n\nRemoção do registro de chave "{ID_REMOCAO}"')
    TAMANHO_ARQ = arquivo_dados.seek(0, os.SEEK_END)
    
    arquivo_dados.seek(TAMANHO_CABECALHO, os.SEEK_SET)
    
    naoAchou = True
    iterador = 0
    while naoAchou == True:
        iterador += 1
        
        # Pega a posicao do tamanho do registro
        posicao_tamanho_registro = arquivo_dados.tell()

        # Pega o tamanho do Registro
        TOTALREG = arquivo_dados.read(TAMANHO_TAMREGISTRO)

        # Pega a posicao inicial do registro antes de ler o ID
        posicao_inicio = arquivo_dados.tell()

        # Pega o registro inteiro, depois cria uma lista separando campos
        registro = arquivo_dados.read(int.from_bytes(TOTALREG)).decode('utf-8')
        registro_em_lista = registro.split('|')

        if registro_em_lista[0] == ID_REMOCAO:
            arquivo_dados.seek(posicao_inicio, os.SEEK_SET)
            
            arquivo_dados.write('*'.encode('utf-8'))
            print(f'Registro removido! ({int.from_bytes(TOTALREG)} bytes)')
            print(f'Local: offset = {posicao_tamanho_registro} bytes ({hex(posicao_tamanho_registro)})')
            insereNoCabecalho(posicao_tamanho_registro.to_bytes(4), int.from_bytes(TOTALREG))
            naoAchou = False

        # Pula para o próximo registro (set na posição onde fica o tamanho do registro anterior e depois pula o valor em bytes)
        arquivo_dados.seek(posicao_inicio, os.SEEK_SET)
        arquivo_dados.seek(int.from_bytes(TOTALREG), os.SEEK_CUR)
        #print(f'Posição do seek depois de pular o registro {arquivo_dados.tell()}')

        if arquivo_dados.tell() >= TAMANHO_ARQ:
            print('Erro: registro não encontrado!')
            naoAchou = False

remove(str(99))

arquivo_dados.close()