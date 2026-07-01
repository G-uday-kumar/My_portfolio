from django.db import models

# Create your models here.
class Projects(models.Model):
    Project_name=models.CharField(max_length=200)
    discription=models.CharField(max_length=200)


    def __str__(self):
        return self.Project_name

class Certifications(models.Model):
    certi=models.CharField(max_length=200)
    dis=models.CharField(max_length=200)
    def __str__(self):
        return self.certi

