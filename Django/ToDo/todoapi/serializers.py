from rest_framework import serializers

from .models import Tasks   # Importing model

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tasks
        fields=["id","task","is_completed",'date']
