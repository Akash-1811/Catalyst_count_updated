from django.db import models

# Create your models here.

class Catalyst_User(models.Model):
    firt_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    user_name = models.CharField(max_length=20,blank=True,null=True)
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return str(self.firt_name)

    def register(self):
        self.save()

    @staticmethod
    def get_user_by_username(username):
        try:
            return Catalyst_User.objects.get(user_name=username)
        except:
            return False
