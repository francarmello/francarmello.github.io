# 📊 Projeto BI Mercado Financeiro

Sistema completo de Business Intelligence desenvolvido com dados públicos do mercado financeiro brasileiro.

O projeto contempla coleta automatizada de dados, modelagem em Data Warehouse, ETL, análise e dashboard executivo.

---

## Objetivo

Construir um pipeline completo de BI utilizando tecnologias amplamente utilizadas no mercado:

- Python
- Pandas
- PostgreSQL
- SQL
- ETL
- Power BI
- GitHub Pages

---

## Arquitetura do Projeto

Fluxo completo:

Yahoo Finance

↓  

Python

↓  

Pandas

↓  

PostgreSQL

↓  

Data Warehouse

├── dim_empresa  
├── dim_tempo  
└── fato_cotacoes  

↓  

Power BI

↓  

Dashboard

---

## Tecnologias Utilizadas

- Python
- yfinance
- Pandas
- PostgreSQL
- SQL
- Power BI
- GitHub Pages

---

## Principais análises

✔ Evolução histórica dos ativos

✔ Ranking de performance acumulada

✔ Heatmap mensal

✔ Comparação risco x retorno

✔ Indicadores de volatilidade

✔ KPIs executivos

---

## Estrutura do projeto

```txt
Projeto_BI_Mercado

├── dashboard
│   └── dashboard.pbix

├── imagens
│   ├── dashboard.png
│   ├── pipeline.png
│   └── modelo_estrela.png

├── scripts
│   └── coleta_mercado.py

├── sql
│   └── modelo_dw.sql

├── index.html

└── README.md