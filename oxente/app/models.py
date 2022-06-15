from django.db import models

class Anime(models.Model):
  name = models.CharField(max_length=255, default="")
  studio = models.CharField(max_length=255, default="")
  theme = models.CharField(max_length=255, default="")
  tags = models.CharField(max_length=255, default="")
  source = models.CharField(max_length=255, default="")
  rating = models.CharField(max_length=255, default="")
  year = models.CharField(max_length=255, default="")
  demographic = models.CharField(max_length=255, default="")
  status = models.CharField(max_length=255, default="")
  eps = models.CharField(max_length=255, default="")
  eps_avg_duration_in_min = models.CharField(max_length=255, default="")
  rated_by = models.CharField(max_length=255, default="")
  
  def __str__(self):
    return self.name