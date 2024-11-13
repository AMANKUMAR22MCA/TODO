from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        # Create a new user instance with the validated data
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
      
        )
        # Set the password (will automatically hash it)
        user.set_password(validated_data['password'])
        user.save()
        return user
