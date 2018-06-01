from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField (max_length = 128)
    email = models.EmailField(max_length = 128)

    def __str__(self):
        return "first name: %s\t  last name: %s\t email: %s\n" % (self.first_name, self.last_name, self.email)
