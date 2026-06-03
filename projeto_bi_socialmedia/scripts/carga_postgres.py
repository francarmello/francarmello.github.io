import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

base=(
    Path(__file__)
    .resolve()
    .parent
    .parent
)

arquivo=(

    base/

    "dados_brutos"/

    "social_unificado.csv"

)

df=pd.read_csv(arquivo)

print(df.head())

engine=create_engine(

"postgresql+psycopg2://postgres:Senha123@localhost/social_bi"

)

df.to_sql(

    "stg_games_social",

    engine,

    schema="social",

    if_exists="replace",

    index=False

)

print(
    "Carga concluída"
)