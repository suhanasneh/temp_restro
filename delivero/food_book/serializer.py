from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    phone_no = serializers.CharField(max_length=50)

