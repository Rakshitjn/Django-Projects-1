from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://th.bing.com/th/id/R0805d07b70205857a5d61233c4367aa3?rik=WiEAj2ucqd4%2bow&riu=http%3a%2f%2fwww.dirtyapronrecipes.com%2fwp-content%2fuploads%2f2015%2f10%2ffood-placeholder.png&ehk=%2fDEsN86Sice1qoWX66c3zxNDjukANZCb9EhIWD0PJP4%3d&risl=&pid=ImgRaw')
    
    def __str__(self):
        return self.item_name