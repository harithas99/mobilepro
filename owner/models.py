from django.db import models

# Create your models here.
class Mobiles(models.Model):
    mobile_name=models.CharField(max_length=120,unique=True)
    colour=models.CharField(max_length=120,unique=True)
    battery=models.PositiveIntegerField()
    storage=models.PositiveIntegerField()
    ram=models.PositiveIntegerField()
    processor=models.PositiveIntegerField()
    weight=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.mobile_name

