# YouTube Gaming Analytics Dashboard

## Objetivo

Analisar quais jogos geram mais audiência e engajamento no YouTube Gaming entre 2018 e 2026.

## Tecnologias

- Python
- YouTube Data API
- PostgreSQL
- SQL
- Power BI

## Pipeline

YouTube API
→ Python ETL
→ PostgreSQL
→ Data Warehouse
→ Power BI

## Modelo Estrela

(imagem)

## Dashboard

(imagem)

## Principais Insights

- Minecraft lidera em visualizações.
- Techno Gamerz é o canal com maior audiência.
- O engajamento médio observado foi de 2,58%.

## Como executar

```bash
pip install -r requirements.txt
py scripts/coleta_youtube.py
py scripts/carga_postgres.py