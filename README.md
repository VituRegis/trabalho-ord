# trabalho-ord
Trabalho de Organização e Recuperação de Dados para realizar busca, inserção e remoção de dados em um arquivo .dat

**Requisitos solicitados:**
- Busca de um jogo pelo IDENTIFICADOR;
- Inserção de um novo jogo;
- Remoção de um jogo.

**Forma de execução:**
```python programa.py -e arquivo_operacoes```

**Formato do Arquivo de Operações:**
```
b 22
i 147|Resident Evil 2|1998|Survival horror|Capcom|PlayStation|
r 99
```

**b** -> Busca o registro na chave '22' <br>
**i** -> Insere o registro do jogo com identificador 147 <br>
**r** -> Remove o registro de chave '99' <br>

**Gerenciar os espaços dísponiveis:** <br>
    A remoção vai ser lógica e será necessário armazenar o espaço resultante da remoção na LED(Lista de Espaços Disponíveis). Os ponteiros devem ser gravados como inteiros de 4 bytes. O programa deve implementar todos os mecanismos de gerenciamento de LED, usando o worst-fit. Quando inserir novos registros a LED deve ser consultada, caso ache espaço o registro será inserido nesse espaço e a sobra(se for maior que 10 bytes) será reinserida na LED. <br>

**Impressão da LED:** <br>
A impressão da LED deve ser feita com o seguinte comando: <br>
```python programa.py -p```
