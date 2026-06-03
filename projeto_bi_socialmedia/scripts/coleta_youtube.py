from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
from pathlib import Path
import time

API_KEY="AIzaSyAnOxi4F52pVhwQ7ppC86YZLr3rWkawmJ8"

youtube=build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

jogos=[

"Dead by Daylight",
"World of Warcraft",
"EA Sports FC 26",
"Call of Duty Warzone",
"Apex Legends",
"Valorant",
"Overwatch",
"Counter Strike 2",
"League of Legends",
"Rocket League",
"Grand Theft Auto V",
"Minecraft",
"Fortnite",
"Dota 2"

]

dados=[]
videos_vistos=set()

for jogo in jogos:

    print(f"\nColetando: {jogo}")

    contador=0
    nextPageToken=None

    while contador<100:

        try:

            response=(

                youtube.search().list(

                    q=f"{jogo} gameplay",

                    part="snippet",

                    type="video",

                    maxResults=50,

                    order="viewCount",

                    pageToken=nextPageToken,

                    publishedAfter=
                    "2018-01-01T00:00:00Z"

                )

                .execute()

            )

        except HttpError as e:

            erro=str(e)

            if "per day" in erro:

                print(
                    "\nCOTA DIÁRIA ESGOTADA"
                )

                exit()

            print(e)

            time.sleep(20)

            continue


        ids=[]

        videos=[]

        for item in response["items"]:

            if contador>=100:
                break

            try:

                vid=item["id"]["videoId"]

                if vid in videos_vistos:
                    continue

                videos_vistos.add(vid)

                ids.append(vid)

                videos.append(item)

            except:
                pass

        # UMA chamada para até 50 vídeos

        detalhes=(

            youtube.videos()

            .list(

                part="statistics",

                id=",".join(ids)

            )

            .execute()

        )

        stats_map={

            x["id"]:x.get(
                "statistics",{}
            )

            for x in detalhes["items"]

        }

        for item in videos:

            if contador>=100:
                break

            vid=item["id"]["videoId"]

            stats=stats_map.get(
                vid,
                {}
            )

            snippet=item["snippet"]

            dados.append({

                "video_id":vid,

                "jogo":jogo,

                "titulo":
                snippet["title"],

                "canal":
                snippet[
                    "channelTitle"
                ],

                "data":
                snippet[
                    "publishedAt"
                ],

                "visualizacoes":
                int(
                    stats.get(
                        "viewCount",
                        0
                    )
                ),

                "likes":
                int(
                    stats.get(
                        "likeCount",
                        0
                    )
                ),

                "comentarios":
                int(
                    stats.get(
                        "commentCount",
                        0
                    )
                ),

                "plataforma":
                "YouTube"

            })

            contador+=1

            print(
                f"{contador}/100",
                end="\r"
            )

        nextPageToken=(
            response.get(
                "nextPageToken"
            )
        )

        if not nextPageToken:
            break

        time.sleep(2)

df=pd.DataFrame(dados)

base=(
Path(__file__)
.resolve()
.parent
.parent
)

arquivo=(
base/
"dados_brutos"/
"youtube_games.csv"
)

df.to_csv(
arquivo,
index=False,
encoding="utf-8-sig"
)

print(df.shape)
print("arquivo salvo")