from google.cloud import storage

def envia_arquivo_bucket(nome_bucket:str, caminho_arquivo:str, nome_arquivo_destino:str):
    """
    Recebe um arquivo e o envia para o bucket de destino no Google Cloud storage
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(nome_bucket)
    blob = bucket.blob(nome_arquivo_destino)
    blob.upload_from_file(caminho_arquivo)