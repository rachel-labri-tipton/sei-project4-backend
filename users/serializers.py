from xml.dom import ValidationErr
from rest_framework import serializers
from users.models import CommunityUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import IsAdminUser


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityUser
        fields = ('username', 'first_name',
                  'last_name', 'password', 'password_repeat', 'email', 'is_staff_writer', 'is_communityleader')

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
            'email': {'required': True}
        }

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CommunityUser.objects.all())]
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    password_repeat = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):

        if attrs['password'] != attrs['password_repeat']:
            raise serializers.ValidatioError(
                {"password": "Password fields don't match."}
            )

        return attrs

    def create(self, data):
        user = CommunityUser.objects.create_user(
            username=data['username'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data[
                'last_name'],
            email=data['email']

        )

        user.set_password(data['password'])

        # save serialized user to DB
        user.save()

        return user


class ProfileEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityUser
        fields = ('username', 'first_name',
                  'last_name', 'email', 'bio',)

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'username': {'required': True},
            'email': {'required': True}
        }

    def validate(self, attrs):
        request = self.context.get("request")
        username = self.context.get("username")
        print("attributes", attrs)
        if request and hasattr(request, "user"):
            if attrs['username'] != request.user.username:
                raise serializers.ValidationError({
                    "not_user": "Woops! What are you doing here? Only the person who made this profile can update it."
                })

        print("attributes", attrs)

        return attrs
#
        # request = self.context.get("request")
        # if request and hasattr(request, "user"):
        #     if not request.user.is_premium:
        #         raise serializers.ValidationError({
        #             "is_premium": "Only premium users can create and update books."
        #         })

        # return attrs

    def update(self, userprofile, data):

        userprofile.username = data.get("username", userprofile.username)
        userprofile.first_name = data.get(
            "first_name", userprofile.first_name)
        userprofile.last_name = data.get(
            "last_name", userprofile.last_name)
        userprofile.email = data.get("email", userprofile.email)
        userprofile.bio = data.get("bio", userprofile.bio)

    # save to the database
        userprofile.save()
        print("userprofile", userprofile.email)
    # render to the api
        return userprofile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = ('username', 'first_name',
                  'last_name', 'bio', 'profile_image')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = ('username', 'password')
