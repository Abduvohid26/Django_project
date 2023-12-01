from django.db import models

# Create your models here.


    
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

