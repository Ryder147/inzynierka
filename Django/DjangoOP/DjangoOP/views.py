from django.http import JsonResponse
import json
from django.core import serializers

from .models import User, avBooked
from .serializers import UserSerializer, BookedSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

@api_view(['GET','POST'])
def User_List(request,format=None):
    #get all the users
    #serialize them 
    #return json
    if request.method=='GET':
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response({f'Users ':serializer.data})
    
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE']) 
def User_detail(request,id,format=None):
    try:
        user=User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method=='GET':
        serializer = UserSerializer(user)               
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='PUT':
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name=default_storage.save(file.name,file)

    return Response(file_name)


@api_view(['GET'])
def Booked_List(request,format=None):
    
    if request.method=='GET':
        booked=avBooked.objects.all()
        serializer=BookedSerializer(booked,many=True)
        return Response({f'Users with reserved dates':serializer.data})    
    

@api_view(['GET','POST','DELETE']) 
def Booked_detail(request,id,format=None):
    try:
        user=User.objects.get(pk=id)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method=='GET':
        try:
            booked=avBooked.objects.filter(user_id=id)
        except avBooked.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookedSerializer(booked,many=True)               
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method=='POST':
               
        newdate = avBooked.objects.create(user=user,date_booked=request.data.get('date_booked'))
        return Response(status=status.HTTP_201_CREATED)       
   
    
    elif request.method=='DELETE':
        try:
            booked=avBooked.objects.filter(user_id=id)
        except avBooked.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            date_delete=request.data.get('date_booked')
            delete=booked.get(date_booked=date_delete)
        except avBooked.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
