from app.models import Anime
import pandas as pd
animeAtual = []
data = pd.read_csv("./archive/anime-list.csv")
colunas = ['name', 'studio', 'theme', 'tags', 'source', 'rating', 'year', 'demographic', 'status', 'eps', 'eps_avg_duration_in_min', 'rated_by']

for i in range(len(data)):
  for j in colunas:
    animeAtual.append(data[j][i])
  Anime.objects.create(name=animeAtual[0], studio=animeAtual[1], theme=animeAtual[2], tags=animeAtual[3], source=animeAtual[4], rating=animeAtual[5], year=animeAtual[6], demographic=animeAtual[7], status=animeAtual[8], eps=animeAtual[9], eps_avg_duration_in_min=animeAtual[10], rated_by=animeAtual[11])
  animeAtual = []
