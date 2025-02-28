from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'telegram_chat_id', 'password', 'password2']

    def validate(self, attrs):
        if attrs.get("password")!=attrs.get("password2"):
            raise serializers.ValidationError({'password2': "Passwords does not match"})
        attrs.pop('password2')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AllAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username', 'telegram_chat_id']