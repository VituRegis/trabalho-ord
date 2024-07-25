import os

TAMANHO_CABECALHO = 4
TAMANHO_TAMREGISTRO = 2

arquivo_dados = open('dados.dat','br+')

def insereNoCabecalho(offset, offset_inteiro):
    arquivo_dados.seek(0, os.SEEK_SET)
    cabecalho = arquivo_dados.read(4)
    cabecalho_inteiro = int.from_bytes(cabecalho)

    # Cabecalho inicial só remove o anterior substituindo pelo atual
    if cabecalho_inteiro == 4294967295 or 0: # esse numero é o cabecalho inicial da LED
        arquivo_dados.seek(0, os.SEEK_SET)
        arquivo_dados.write(offset)
    else:
        arquivo_dados.seek(0, os.SEEK_SET)
        arquivo_dados.write(offset)

        arquivo_dados.seek(offset_inteiro, os.SEEK_SET)
        arquivo_dados.seek(4, os.SEEK_CUR)
        arquivo_dados.write(cabecalho)

def remove(ID_REMOCAO):
    id_remocao_str = str(ID_REMOCAO)

    print(f'\n\nRemoção do registro de chave "{id_remocao_str}"')
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
        

        registro_bytes = arquivo_dados.read(int.from_bytes(TOTALREG))

        try:
            registro = registro_bytes.decode('utf-8')

            registro_em_lista = registro.split('|')
        
            if registro_em_lista[0] == id_remocao_str:
                arquivo_dados.seek(posicao_inicio, os.SEEK_SET)
                
                arquivo_dados.write('*|'.encode('utf-8'))
                print(f'Registro removido! ({int.from_bytes(TOTALREG)} bytes)')
                print(f'Local: offset = {posicao_tamanho_registro} bytes ({hex(posicao_tamanho_registro)})')
                insereNoCabecalho(posicao_tamanho_registro.to_bytes(4, byteorder='big'), posicao_tamanho_registro)
                naoAchou = False
                break
        except UnicodeDecodeError: #ignora os campos apagados previamente
            ...

        # Pula para o próximo registro (set na posição onde fica o tamanho do registro anterior e depois pula o valor em bytes)
        arquivo_dados.seek(posicao_inicio, os.SEEK_SET)
        arquivo_dados.seek(int.from_bytes(TOTALREG), os.SEEK_CUR)

        if arquivo_dados.tell() >= TAMANHO_ARQ:
            print('Erro: registro não encontrado!')
            naoAchou = False