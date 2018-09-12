from rest_framework import serializers
from .models import Book,Summary

class BookSerializer(serializers.ModelSerializer):

 class Meta:
     fields = '__all__'
     model = Book

class SummarySerializer(serializers.ModelSerializer):

 class Meta:
     fields = '__all__'
     model = Summary
