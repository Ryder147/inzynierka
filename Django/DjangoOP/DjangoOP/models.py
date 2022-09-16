from django.db import models 

# python manage.py makemigrations DjangoOP
# python manage.py migrate




class User(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    birth_date=models.DateField(auto_now=False)
    photo_name=models.CharField(max_length=100, blank=True, null=True)
    availability_start=models.DateField(auto_now=False,blank=True, null=True)
    availability_end=models.DateField(auto_now=False,blank=True, null=True)
    
    def __str__(self):
        return f'{self.id} {self.user_name}'   

class avBooked(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
    date_booked= models.DateField(auto_now=False,null=True,blank=True)

    def __str__(self):
        return f'{self.user.id} {self.user.name} {self.date_booked}'