from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """
        Create a new user with encrypted password and return it.
        :param validated_data:
        :return: created user
        :rtype: User
        """
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """
        Update a user, setting the password correctly and return it.
        :param instance:
        :param validated_data:
        :return: updated user
        :rtype: User
        """
        password = validated_data.pop("password", None)

        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}}
