import pandas as pd
from pathlib import Path

base = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

youtube = pd.read_csv(

    base /
    "dados_brutos" /
    "youtube_games.csv"

)

# padronização

youtube["plataforma"]="YouTube"

# garantir tipos

youtube["visualizacoes"] = pd.to_numeric(
    youtube["visualizacoes"],
    errors="coerce"
).fillna(0)

youtube["likes"] = pd.to_numeric(
    youtube["likes"],
    errors="coerce"
).fillna(0)

youtube["comentarios"] = pd.to_numeric(
    youtube["comentarios"],
    errors="coerce"
).fillna(0)

youtube=(
    youtube
    .drop_duplicates(
        subset=["video_id"]
    )
)

arquivo_saida=(

    base/

    "dados_brutos"/

    "social_unificado.csv"

)

youtube.to_csv(

    arquivo_saida,

    index=False,

    encoding="utf-8-sig"

)

print("Arquivo criado")

print(youtube.shape)

print(
    youtube.head()
)