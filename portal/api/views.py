from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics, permissions, mixins
from rest_framework.generics import CreateAPIView

from portal.api.serializers import BookSerializer, CategorySerializer, UserSerializer, ExtraSerializer, \
    FeedbackSerializer, ReviewSerializer
from portal.models import Book, Category, Extra, Feedback, Reviews


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


class BooksListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BookSerializer

    def get_queryset(self):
        qs = Book.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(book_name__icontains=query) | Q(book_course_name__icontains=query)).distinct()
        return qs

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class BooksRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CategoryListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CategoryRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ExtrasListView(generics.ListAPIView):
    serializer_class = ExtraSerializer

    def get_queryset(self):
        return Extra.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ExtrasRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ExtraSerializer

    def get_queryset(self):
        return Extra.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class FeedbackAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        return Feedback.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class FeedbackRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        return Feedback.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ReviewAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Reviews.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ReviewRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Reviews.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}