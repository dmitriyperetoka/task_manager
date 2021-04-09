from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from tasks.models import Task
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, max_length=128, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    performers = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(), many=True, allow_empty=False)

    class Meta:
        model = Task
        fields = '__all__'
