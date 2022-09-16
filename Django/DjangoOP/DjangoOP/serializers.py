
from rest_framework import serializers
from .models import User, avBooked

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','user_name','password', 'birth_date','photo_name','availability_start','availability_end']      #robimy tablice w której definiujemy jakie dane będziemy zwracać z obiektu naszego api

class BookedSerializer(serializers.ModelSerializer):
    class Meta:
        model=avBooked
        fields=['user','date_booked']

