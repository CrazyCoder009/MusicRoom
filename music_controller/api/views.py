from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
# Create your views here.

class RoomView(generics.ListAPIView):    #CreateAPIView Creates a room API for crating a room while ListAPIView Lists all available rooms
    queryset = Room.objects.all()     #queries  into the room (return all room objects from Models.py)
    serializer_class = RoomSerializer  #calls from roomserializer