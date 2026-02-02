from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User, AuthProvider


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["full_name", "email", "password", "mobile"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(
            full_name=validated_data.get("full_name"),
            email=validated_data.get("email"),
            mobile=validated_data.get("mobile"),
            auth_provider=AuthProvider.EMAIL,
        )
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=self.context.get("request"), email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        attrs["user"] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name", "email", "mobile", "auth_provider"]
