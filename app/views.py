from django.shortcuts import render
from app.models import Student
from app.serializers import Studentserializer
from rest_framework import viewsets

class StudentViewsets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
