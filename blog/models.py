from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=23)
    phone = models.IntegerField()
    email = models.FloatField(max_length=23)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return 'Massage from'+ self.name 
     
    
class Upload(models.Model):
    name=models.CharField(max_length=50)
    pic=models.FileField(upload_to='images/')
    author=models.CharField(max_length=50)
    upload_date=models.DateTimeField(auto_now_add=True)

