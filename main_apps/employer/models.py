from django.contrib.auth.models import User
from django.db import models

class Employer(User):
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Poste(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='postes')

    def __str__(self):
        return self.title
