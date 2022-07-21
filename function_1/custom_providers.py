import random
from faker.providers import BaseProvider

class produtos(BaseProvider):
    def produto(self):
        return random.choice([
            'Sofa', 'Geladeira', 'Fogao',
            'Vidro', 'Mesa', 'Cama',
            'Cola de sapateiro', 'Desodorante',
            'Coca-cola', 'Caderno', 'Caixa',
            'Monitor', 'Mouse gamer', 'Sapato'
        ])

class vendedores(BaseProvider):
    def vendedor(self):
        return random.choice([
            'Carlos', 'Jefferson', 'Adilson',
            'Cleber', 'Marcela', 'Sheyla',
            'Arlete', 'Elisangela'
        ])