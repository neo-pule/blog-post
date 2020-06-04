from django.urls import path
from blog_for_articles.views import index,admin,home

app_name = 'first_app'

urlpatterns = [
    path('',index),
    path('home',home),
    path('index',admin),

]
