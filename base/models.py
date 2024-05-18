from django.db import models

# Create your models here.
class MyMod(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course=models.CharField( max_length=100)
    phone_number= models.BigIntegerField()
    address =models.TextField()
    email=models.EmailField(null=True)
    batch=models.CharField(null=True,max_length=50)
    qulification=models.CharField(null=True,max_length=50)




    


    
    class Meta:
        db_table = 'stdent'
 