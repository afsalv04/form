from django.db import models
 
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


class login(models.Model):
    email = models.EmailField()
    password = models.CharField()    

    def __str__(self):
        return self.name  
    


# Create your models here.
