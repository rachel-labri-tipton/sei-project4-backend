from rest_framework import serializers
from users.models import CommunityUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityUser
        fields = ('username', 'first_name',
                  'last_name', 'password', 'password_repeat', 'email', 'profile_image', 'is_author', 'is_communityleader')

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
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
            email=data['email'],
            profile_image=data['profile_image']

        )

        user.set_password(data['password'])

        # save serialized user to DB
        user.save()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = ('username', 'password')


class IsAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = ('username', 'is_author')
