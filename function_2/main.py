from google.cloud import bigquery
import os

def ingestao_csv(event, context):
    """Cloud function que é engatilhada por novo arquivo no bucket GCS
       Essa função carrega os dados do arquivo que acabaram de chegar no
       bucket GCS para uma tabela específica do BigQuery
    """

    cliente = bigquery.Client()

    id_tabela = os.getenv('CAMINHO_TABELA')

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField('id_pedido', "INTEGER"),
            bigquery.SchemaField('nome', "STRING"),
            bigquery.SchemaField('sobrenome', "STRING"),
            bigquery.SchemaField('cpf', "STRING"),
            bigquery.SchemaField('data_nascimento', "DATE"),
            bigquery.SchemaField('estado', "STRING"),
            bigquery.SchemaField('email', "STRING"),
            bigquery.SchemaField('telefone', "STRING"),
            bigquery.SchemaField('status_pedido', "BOOLEAN"),
            bigquery.SchemaField('vendedor', "STRING"),
            bigquery.SchemaField('produto', "STRING"),
            bigquery.SchemaField('data_transacao', "DATETIME")
        ],
        write_disposition="WRITE_APPEND",
        skip_leading_rows=1,
        time_partitioning=bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field="data_transacao"
        ),
    )

    uri = f"gs://{event['bucket']}/{event['name']}"

    job_carga = cliente.load_table_from_uri(
        uri, id_tabela, job_config=job_config
    )

    job_carga.result()

    tabela = cliente.get_table(id_tabela)
    
    print("Existem agora {} linhas na tabela {}" \
        .format(tabela.num_rows, id_tabela))

    cliente.query("CALL dataset.criar_staging()").result()