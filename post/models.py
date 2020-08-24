from django.db import models

# Create your models here.

class Catagory(models.Model):
    cat_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.cat_name

class Post(models.Model):
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    count = models.CharField(max_length=10000000000000,unique=True)
    date = models.DateField()
    title = models.CharField(max_length=264,unique=True)
    img_name = models.CharField(max_length=100,unique=True)
    text = models.CharField(max_length=3500,unique=True)

    def __str__(self):
        return self.title

class Visiters(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254,unique=True)
    
    def __str__(self):
        return self.name

