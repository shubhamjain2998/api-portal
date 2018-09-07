from django.contrib import admin

# Register your models here.
from portal.models import Category, Book, Extra, Feedback, Reviews


class BookAdmin(admin.ModelAdmin):
    list_filter = ['book_name', 'book_course_name', 'category']
    list_display = ['book_name', 'book_course_name', 'category']
    search_fields = ['book_name']


admin.site.register(Book, BookAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class ExtraAdmin(admin.ModelAdmin):
    list_filter = ['name', 'category', 'date']
    list_display = ['name', 'category', 'date']
    search_fields = ['name']


admin.site.register(Extra, ExtraAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_filter = ['name', 'subject', 'date']
    list_display = ['name', 'subject', 'date']


admin.site.register(Feedback, FeedbackAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list_filter = ['rating']
    list_display = ['name', 'rating', 'date']


admin.site.register(Reviews, ReviewsAdmin)
