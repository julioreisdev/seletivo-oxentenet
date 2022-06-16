from django.shortcuts import render
from .models import Anime
from django.db.models import Count

def dashboard(request):
  estudios = Anime.objects.values('studio').annotate(qtd=Count('studio')).order_by('-qtd')
  estudiosMaisAnimes = []
  for i in range(5):
    estudiosMaisAnimes.append(estudios[i])
  
  quantidadeAnimes = len(Anime.objects.all())
  
  def converte(i, value):
    valor = ''
    for j in range(len(i['rated_by']) - 1):
      valor = valor + i['rated_by'][j]
    i['rated_by'] = float(valor) * value
  
  animes = Anime.objects.values('name', 'rated_by').order_by()
  animesMaisAvaliados = []
  
  for i in animes:
    if i['rated_by'][len(i['rated_by']) - 1] == 'M':
      converte(i, 1000000)
    elif i['rated_by'][len(i['rated_by']) - 1] == 'K':
      converte(i, 1000)
       
  for i in range(10):
    animesMaisAvaliados.append(animes[i])
  
  return render(request, "index.html", 
                {
                  'quantidadeAnimes': quantidadeAnimes,
                  'estudios': estudiosMaisAnimes,
                  'animes': animesMaisAvaliados,
                })