from django.shortcuts import render
from .models import Anime
import pandas as pd
import numpy as np


def dashboard(request):
  estudios = []
  
  for i in range(len(Anime.objects.all())):
    estudios.append(Anime.objects.all()[i].studio)
  
  dados = np.array(estudios);
  ocorrencias = pd.DataFrame(np.array(np.unique(dados, return_counts=True)).T)
  ocorrencias = ocorrencias.sort_values(by=[1], ascending=False , ignore_index=True)
  
  estudio1 = ocorrencias[0][0]
  estudio2 = ocorrencias[0][1]
  estudio3 = ocorrencias[0][2]
  estudio4 = ocorrencias[0][3]
  estudio5 = ocorrencias[0][4]
  
  quantidadeAnimes = len(Anime.objects.all())
  animeMaiorAvaliacao1 = Anime.objects.all()[0]
  animeMaiorAvaliacao2 = Anime.objects.all()[1]
  animeMaiorAvaliacao3 = Anime.objects.all()[2]
  animeMaiorAvaliacao4 = Anime.objects.all()[3]
  animeMaiorAvaliacao5 = Anime.objects.all()[4]
  animeMaiorAvaliacao6 = Anime.objects.all()[5]
  animeMaiorAvaliacao7 = Anime.objects.all()[6]
  animeMaiorAvaliacao8 = Anime.objects.all()[7]
  animeMaiorAvaliacao9 = Anime.objects.all()[8]
  animeMaiorAvaliacao10 = Anime.objects.all()[9] 
  return render(request, "index.html", {'quantidadeAnimes': quantidadeAnimes, 'animeMaiorAvaliacao1': animeMaiorAvaliacao1, 'animeMaiorAvaliacao2': animeMaiorAvaliacao2, 'animeMaiorAvaliacao3': animeMaiorAvaliacao3, 'animeMaiorAvaliacao4': animeMaiorAvaliacao4, 'animeMaiorAvaliacao5': animeMaiorAvaliacao5, 'animeMaiorAvaliacao6': animeMaiorAvaliacao6, 'animeMaiorAvaliacao7': animeMaiorAvaliacao7, 'animeMaiorAvaliacao8': animeMaiorAvaliacao8, 'animeMaiorAvaliacao9': animeMaiorAvaliacao9, 'animeMaiorAvaliacao10': animeMaiorAvaliacao10, 'estudio1': estudio1, 'estudio2': estudio2, 'estudio3': estudio3, 'estudio4': estudio4, 'estudio5': estudio5})