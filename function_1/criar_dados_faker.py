import random    
from faker import Faker
from custom_providers import produtos, vendedores

def criar_dados_csv():    
    
    fake = Faker('pt_BR')

    #Adicionando providers ao faker
    fake.add_provider(produtos)
    fake.add_provider(vendedores)

    #Nomes dos campos que iremos gerar
    nomes_campos = [
        'aba', 'first_name', 'last_name', 'cpf', 'date_of_birth',
        'estado_sigla', 'ascii_free_email', 'phone_number', 'pybool', 'vendedor',
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

    print('Dados criados!')

    return dados