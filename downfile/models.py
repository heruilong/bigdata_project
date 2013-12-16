from django.db import models

# Create your models here.
class GeneSearch(models.Model):
    clade = models.CharField(max_length = 15)
    genome = models.CharField(max_length =15)
    seqType = models.CharField(max_length = 15)
