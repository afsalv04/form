from django.db import models
from django.contrib.auth.models import User

 
# class contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()


# class login(models.Model):
#     email = models.EmailField()
#     password = models.CharField()    


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.user.get_full_name() or self.user.username



# Create your models here.
