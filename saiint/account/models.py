from django.db import models

# Create your models here.
class User (models.Model):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    user_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254, null = 'FALSE')

    def __str__(self):
        return self.user_name
