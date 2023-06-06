from django.db import models

# Create your models here.
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    address=models.CharField(max_length=400)
    city=models.CharField(max_length=40)
    state=models.CharField(max_length=40)
    pincode=models.BigIntegerField()

    def __str__(self):
        return(f"{self.first_name}{self.last_name}")
