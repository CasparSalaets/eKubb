from django.db import models

class eKubb(models.Model):
    name = models.CharField(max_length=100)
    # artist = models.ForeignKey(Artists)
    release_date = models.DateField()
    
