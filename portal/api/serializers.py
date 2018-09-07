from portal.models import Book, Category, Extra, Feedback, Reviews
from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]


class BookSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = [
            'url',
            'pk',
            'book_name',
            'book_course_name',
            'category',
            'img',
            'file',
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = [
            'url',
            'pk',
            'name',
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class ExtraSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Extra
        fields = [
            'url',
            'pk',
            'name',
            'category',
            'file',
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class FeedbackSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Feedback
        fields = [
            'url',
            'pk',
            'name',
            'email',
            'phone',
            'subject',
            'message',
            'date'
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class ReviewSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Reviews
        fields = [
            'url',
            'pk',
            'name',
            'rating',
            'message',
            'date'
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)