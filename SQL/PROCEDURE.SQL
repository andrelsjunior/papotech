CREATE OR REPLACE PROCEDURE
  camada_raw.criar_staging()
BEGIN
INSERT INTO
  `gglobo-coe-govdados-dev-qa.dataform.staging`
WITH
  dedup AS (
  SELECT
    id_pedido,
    nome,
    sobrenome,
    REGEXP_REPLACE(cpf, '[^0-9]', '') AS cpf,
    data_nascimento,
    estado,
    email,
    REGEXP_REPLACE(telefone, '[^0-9]', '') AS telefone,
    status_pedido,
    vendedor,
    produto,
    data_transacao,
    ROW_NUMBER() OVER (PARTITION BY id_pedido ORDER BY data_transacao ASC) AS rn
  FROM
    `gglobo-coe-govdados-dev-qa.dataform.teste` )
SELECT
  * EXCEPT(rn)
FROM
  dedup
WHERE
  rn=1;
END;