import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

ativos = [
    "PETR4.SA",
    "VALE3.SA",
    "ITUB4.SA",
    "BBDC4.SA",
    "MGLU3.SA"
]

lista_dfs = []

for ativo in ativos:

    print(f"Baixando {ativo}")

    df = yf.download(
        ativo,
        start="2020-01-01",
        auto_adjust=False,
        progress=False
    )

    # transforma a data em coluna
    df = df.reset_index()

    # remove MultiIndex das colunas
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    # adiciona ticker
    df["ticker"] = ativo

    lista_dfs.append(df)

dados = pd.concat(
    lista_dfs,
    ignore_index=True
)

print(dados.head())

engine = create_engine(
    "postgresql://postgres:13473553832@localhost:5432/mercado_bi"
)

dados.to_sql(
    "stg_cotacoes",
    engine,
    schema="bolsa",
    if_exists="replace",
    index=False
)

print("Dados enviados com sucesso!")