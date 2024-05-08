from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book id")
    title=serializers.CharField(label="Enter Book title")
    author=serializers.CharField(label="Enter Author Name")