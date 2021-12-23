from django.contrib.auth import get_user_model
from rest_framework import serializers

# from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "password", "first_name", "last_name")
        # fields = ('id', 'email', 'password', 'username', 'first', 'last',
        #           'date_joined', 'last_login', 'is_admin', 'is_staff')
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

        # This create method will be used for model creation

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
