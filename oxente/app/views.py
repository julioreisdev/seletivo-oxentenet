from django.shortcuts import render
from .models import Anime
from django.db.models import Count

def dashboard(request):
  quantidadeAnimes = len(Anime.objects.all())
  estudios = Anime.objects.values('studio').annotate(qtd=Count('studio')).order_by('-qtd')[:5]
  
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
                  'estudios': estudios,
                  'animes': animesMaisAvaliados,
                })