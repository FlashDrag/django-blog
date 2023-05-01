from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # 1st slug - path converter, that converts the slug to a string
    # 2nd slug - keyword name, matches the 'slug' parameter in the view
    # https://docs.djangoproject.com/en/3.2/topics/http/urls/#path-converters
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
