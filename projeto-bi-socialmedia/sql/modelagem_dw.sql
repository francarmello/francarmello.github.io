-- ==========================================
-- LIMPEZA
-- ==========================================

DROP TABLE IF EXISTS social.fato_engajamento_games;

DROP TABLE IF EXISTS social.dim_tempo;

DROP TABLE IF EXISTS social.dim_jogo;


-- ==========================================
-- DIM JOGO
-- ==========================================

CREATE TABLE social.dim_jogo AS

SELECT DISTINCT

ROW_NUMBER() OVER(
ORDER BY jogo
) jogo_id,

jogo

FROM social.stg_games_social

WHERE jogo IS NOT NULL;



ALTER TABLE social.dim_jogo
ADD PRIMARY KEY(jogo_id);



-- ==========================================
-- DIM TEMPO
-- ==========================================

CREATE TABLE social.dim_tempo AS

SELECT DISTINCT

ROW_NUMBER() OVER(
ORDER BY data::timestamp
) tempo_id,

data::timestamp AS data,

EXTRACT(
YEAR FROM data::timestamp
) ano,

EXTRACT(
MONTH FROM data::timestamp
) mes,

EXTRACT(
QUARTER FROM data::timestamp
) trimestre

FROM social.stg_games_social

WHERE data IS NOT NULL;



ALTER TABLE social.dim_tempo
ADD PRIMARY KEY(tempo_id);



-- ==========================================
-- FATO
-- ==========================================

CREATE TABLE social.fato_engajamento_games AS

SELECT

ROW_NUMBER() OVER() AS fato_id,

j.jogo_id,

t.tempo_id,

COALESCE(
s.titulo,
'Sem título'
) titulo,

COALESCE(
s.canal,
'Canal desconhecido'
) canal,

COALESCE(
s.visualizacoes,
0
) visualizacoes,

COALESCE(
s.likes,
0
) likes,

COALESCE(
s.comentarios,
0
) comentarios

FROM social.stg_games_social s

LEFT JOIN social.dim_jogo j
ON s.jogo=j.jogo

LEFT JOIN social.dim_tempo t
ON
s.data::timestamp =
t.data;



ALTER TABLE social.fato_engajamento_games
ADD PRIMARY KEY(fato_id);



ALTER TABLE social.fato_engajamento_games
ADD CONSTRAINT fk_jogo

FOREIGN KEY(jogo_id)

REFERENCES social.dim_jogo(
jogo_id
);



ALTER TABLE social.fato_engajamento_games
ADD CONSTRAINT fk_tempo

FOREIGN KEY(tempo_id)

REFERENCES social.dim_tempo(
tempo_id
);



-- ==========================================
-- VALIDAÇÕES
-- ==========================================

SELECT COUNT(*)
FROM social.dim_jogo;


SELECT COUNT(*)
FROM social.dim_tempo;


SELECT COUNT(*)
FROM social.fato_engajamento_games;


SELECT *
FROM social.fato_engajamento_games
LIMIT 10;