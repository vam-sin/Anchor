
from django.urls import path,include
from . import views

urlpatterns = [
    path('create',views.create,name='create'),
    path('account',views.account,name='account'),
    path('<int:news_id>',views.detail,name="detail"),
    path('<int:news_id>/love',views.love,name='love'),
    path('',views.login,name='login'),
    path('<int:news_id>/add_comment_to_post',views.add_comment_to_post,name='add_comment_to_post'),
]
