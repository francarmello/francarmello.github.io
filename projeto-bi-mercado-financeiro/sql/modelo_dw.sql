/*
Projeto BI Mercado Financeiro

Pipeline:

Yahoo Finance
→ Python
→ PostgreSQL
→ Data Warehouse
→ Power BI

Autor: Francisco Carmello
Data: 2026
*/

-- =========================================
-- PROJETO BI MERCADO FINANCEIRO
-- DATA WAREHOUSE
-- =========================================

-- cria schema
CREATE SCHEMA IF NOT EXISTS bolsa;


-- =========================================
-- DIM_EMPRESA
-- =========================================

DROP TABLE IF EXISTS bolsa.dim_empresa;

CREATE TABLE bolsa.dim_empresa (

    empresa_id SERIAL PRIMARY KEY,

    ticker VARCHAR(20) UNIQUE,

    empresa VARCHAR(100),

    setor VARCHAR(100)

);


INSERT INTO bolsa.dim_empresa
(ticker,empresa,setor)

VALUES

('PETR4.SA','Petrobras','Petróleo'),

('VALE3.SA','Vale','Mineração'),

('ITUB4.SA','Itaú','Bancos'),

('BBDC4.SA','Bradesco','Bancos'),

('MGLU3.SA','Magazine Luiza','Varejo');



-- =========================================
-- DIM_TEMPO
-- =========================================

DROP TABLE IF EXISTS bolsa.dim_tempo;


CREATE TABLE bolsa.dim_tempo AS

SELECT DISTINCT

    CAST("Date" AS DATE) AS data,

    EXTRACT(YEAR FROM CAST("Date" AS DATE)) AS ano,

    EXTRACT(MONTH FROM CAST("Date" AS DATE)) AS mes,

    EXTRACT(QUARTER FROM CAST("Date" AS DATE)) AS trimestre,

    EXTRACT(DOW FROM CAST("Date" AS DATE)) AS dia_semana

FROM bolsa.stg_cotacoes;



-- =========================================
-- FATO_COTACOES
-- =========================================

DROP TABLE IF EXISTS bolsa.fato_cotacoes;


CREATE TABLE bolsa.fato_cotacoes AS

WITH base AS (

    SELECT

        CAST("Date" AS DATE) AS data,

        ticker,

        "Open" AS abertura,

        "Close" AS fechamento,

        "High" AS maxima,

        "Low" AS minima,

        "Volume" AS volume,

        (

            ("Close" -

                LAG("Close") OVER(

                    PARTITION BY ticker

                    ORDER BY "Date"

                )

            )

            /

            LAG("Close") OVER(

                PARTITION BY ticker

                ORDER BY "Date"

            )

        ) AS retorno


    FROM bolsa.stg_cotacoes

)


SELECT

    b.data,

    e.empresa_id,

    b.abertura,

    b.fechamento,

    b.maxima,

    b.minima,

    b.volume,

    b.retorno

FROM base b

INNER JOIN bolsa.dim_empresa e

ON b.ticker=e.ticker;



-- =========================================
-- TESTES
-- =========================================


SELECT * FROM bolsa.dim_empresa;

SELECT * FROM bolsa.dim_tempo LIMIT 10;

SELECT * FROM bolsa.fato_cotacoes LIMIT 10;