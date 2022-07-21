from faker import Faker
from custom_providers import produtos, vendedores
from envia_arquivo_bucket import envia_arquivo_bucket
import random
import os

nome_bucket = os.getenv('NOME_BUCKET')

fake = Faker('pt_BR')

#Adicionando providers ao faker
fake.add_provider(produtos)
fake.add_provider(vendedores)

#Nomes dos campos que iremos gerar
nomes_campos = [
    'aba', 'first_name', 'last_name', 'cpf', 'date_of_birth',
    'estado_sigla', 'free_email', 'phone_number', 'pybool', 'vendedor',
    'produto', 'date_time_this_month'
    ]

#List comprehension para gerar o jinja com o nome da coluna.
colunas_dados = [f'{{{{{item}}}}}' for item in nomes_campos]

dados = fake.csv(
    data_columns=colunas_dados,
    header=nomes_campos,
    num_rows=random.randint(2000,6000),
    include_row_ids=False
)

nome_arquivo = f'dados_marketing_{random.randint(1, 10000)}.csv'

with open('/tmp/' + nome_arquivo, "w") as csv: 
    csv.write(dados)

with open('/tmp/' + nome_arquivo, 'r') as arquivo:
    envia_arquivo_bucket(nome_bucket, arquivo, nome_arquivo)