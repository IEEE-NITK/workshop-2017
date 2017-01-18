from django.db import models

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=64)


class Student(models.Model):
    name = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch)
    email = models.EmailField(max_length=254)
    age = models.IntegerField(default=18)

    #add this to above model and show changes in admin page.
    def __str__(self):
        return self.name
