from . import views 
from django.urls import path 

urlpatterns = [
    path('home/', views.posts, name='home'),
    path('info/', views.info, name='info'),
    path('comment/', views.post_comment, name='comment'),
    path('new_article_form/', views.add_article, name='new_article_form'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
]