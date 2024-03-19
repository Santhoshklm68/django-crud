from django.shortcuts import render
from app.models import Student
from app.serializers import Studentserializer
from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

class StudentViewsets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
