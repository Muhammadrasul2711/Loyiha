from django.db import models
class Qurulmalar(models.Model):
    name = models.CharField(max_length=256)
    brand_name = models.CharField(max_length=256)
    price = models.IntegerField()
    img= models.ImageField(upload_to='25')
    def __str__(self):
        return self.brand_name



class Watch(models.Model):
    name = models.CharField(max_length=256)
    img= models.ImageField(upload_to='25')
    title= models.CharField(max_length=256)



class Bacground(models.Model):
    img= models.ImageField(upload_to='img/')
