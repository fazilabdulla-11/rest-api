from rest_framework import serializers
from .models import Book


class Bookserializers(serializers.Modelserializer):
    class meta:
        model = Book 
        fields = '__all__'