# # get data from model--->json
# # users/serializers.py
# from rest_framework import serializers
# from django.contrib.auth import get_user_model, authenticate
# from rest_framework.authtoken.models import Token
# from rest_framework.validators import ValidationError
# from django.contrib.auth.hashers import make_password
# User = get_user_model()


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password','name')
        
#     def validate(self, attrs):
#         username_exists = User.objects.filter(username=attrs["username"]).exists()
#         if username_exists:
#             raise ValidationError("Username has already been used")

#         return super().validate(attrs)
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], name = validated_data['name'])
#         return user

# class ChangePasswordSerializer(serializers.Serializer):
#     model = User
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)
#     def validate_old_password(self, value):
#         user = self.context['request'].user
#         if not user.check_password(value):
#             raise serializers.ValidationError("Old password is not correct")
#         return value

# class UpdateProfileSerializer(serializers.Serializer):
#     new_name = serializers.CharField(required=True)
#     new_email = serializers.CharField(required=True)
#     new_image = serializers.FileField()

# #################################################################



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'name', 'image', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         return super().create(validated_data)



##################################################################################
# newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww


# accounts/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'image']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'password', 'image']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        
        # Save the image if provided
        if 'image' in validated_data:
            user.image = validated_data['image']
        
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'image','is_superuser']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        
        if 'image' in validated_data:
            instance.image = validated_data['image']
        
        instance.save()
        return instance