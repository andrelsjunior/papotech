from envia_arquivo_bucket import envia_arquivo_bucket
from criar_dados_faker import criar_dados_csv
import random
import os

def insere_arquivo_bucket(context, event):
    nome_bucket = os.getenv('NOME_BUCKET')

    dados = criar_dados_csv()

    nome_arquivo = f'dados_marketing_{random.randint(1, 10000)}.csv'

    print('Criando arquivo CSV')
    try:
        with open('/tmp/' + nome_arquivo, "w") as csv: 
            csv.write(dados)
        print(f'{nome_arquivo} foi criado com sucesso')
    except Exception as e:
        print(e)

    print('Enviando arquivo para o bucket do Cloud Storage')
    with open('/tmp/' + nome_arquivo, 'rb') as arquivo:
        envia_arquivo_bucket(nome_bucket, arquivo, nome_arquivo)