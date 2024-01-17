from django.urls import path
from . import views

urlpatterns = [
    path('', views.orel_and_reshka, name='orel_and_reshka'),
    path('post_view/', views.post_view, name='post_view'),
    path('author_view/', views.authors_view, name='author_view'),
]
