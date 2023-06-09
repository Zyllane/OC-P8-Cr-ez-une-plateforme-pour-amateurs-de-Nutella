from django.db import models

# Create your models here.
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=80)
    nutriscore = models.CharField(max_length=1)

class User(models.Model):
    mail = models.CharField(max_length=20,default='')
    password = models.CharField(max_length=16,default='')
    firstname = models.CharField(max_length=20,default='')

    """Vérifier best practice Django vis à vis des mdp"""

class Bookmark(models.Model):
    id_product = models.ForeignKey(Product,on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
