from django.db import models

# Create your models here.
# ORM(Object Relataion mapping)

class my_board( models.Model ):
    createDate = models.DateField()
    writer = models.CharField(max_length=128)
    subject = models.CharField(max_length=255)
    content = models.TextField()