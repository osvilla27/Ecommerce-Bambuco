from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_date):
        password = validated_date.pop('password', None)
        instance = self.Meta.model(**validated_date)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'date_joined', 'get_full_name',
                  'get_short_name']