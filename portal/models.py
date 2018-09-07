from django.core.files.storage import FileSystemStorage
from django.core.validators import MaxValueValidator
from django.db import models
from rest_framework.reverse import reverse as api_reverse


class MediaFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if max_length and len(name) > max_length:
            raise (Exception("name's length is greater than max_length"))
        return name

    def _save(self, name, content):
        if self.exists(name):
            # if the file exists, do not call the superclasses _save method
            return name
        # if the file is new, DO call it
        return super(MediaFileSystemStorage, self)._save(name, content)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    def get_api_url(self, request=None):
        return api_reverse("api-portal:category-retrieve", kwargs={'pk': self.pk}, request=request)


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_course_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images//", storage=MediaFileSystemStorage(), null=True, blank=True)
    file = models.FileField(upload_to="docs//", storage=MediaFileSystemStorage(), null=True, blank=True)

    def __str__(self):
        return str(self.book_name)

    def get_api_url(self, request=None):
        return api_reverse("api-portal:book-retrieve", kwargs={'pk': self.pk}, request=request)


class Extra(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.FileField(upload_to="Extras//", storage=MediaFileSystemStorage(), null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_api_url(self, request=None):
        return api_reverse("api-portal:extras-retrieve", kwargs={'pk': self.pk}, request=request)


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_api_url(self, request=None):
        return api_reverse("api-portal:feedback-rud", kwargs={'pk': self.pk}, request=request)


class Reviews(models.Model):
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_api_url(self, request=None):
        return api_reverse("api-portal:review-rud", kwargs={'pk': self.pk}, request=request)
