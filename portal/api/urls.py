from django.conf.urls import url

from portal.api.views import BooksRetrieveView, BooksListView, CategoryRetrieveView, CategoryListView, CreateUserView, \
    ExtrasListView, ExtrasRetrieveView, FeedbackRUDView, FeedbackAPIView, ReviewAPIView, ReviewRUDView

app_name = 'api-portal'
urlpatterns = [
    url('^register/$', CreateUserView.as_view(), name='user-register'),
    url('^books/$', BooksListView.as_view(), name='books-list'),
    url('^books/(?P<pk>\d+)/$', BooksRetrieveView.as_view(), name='book-retrieve'),
    url('^category/$', CategoryListView.as_view(), name='category-list'),
    url('^category/(?P<pk>\d+)/$', CategoryRetrieveView.as_view(), name='category-retrieve'),
    url('^extra/$', ExtrasListView.as_view(), name='extras-list'),
    url('^extra/(?P<pk>\d+)/$', ExtrasRetrieveView.as_view(), name='extras-retrieve'),
    url('^feedback/$', FeedbackAPIView.as_view(), name='feedback-api'),
    url('^feedback/(?P<pk>\d+)/$', FeedbackRUDView.as_view(), name='feedback-rud'),
    url('^review/$', ReviewAPIView.as_view(), name='review-api'),
    url('^review/(?P<pk>\d+)/$', ReviewRUDView.as_view(), name='review-rud'),
]