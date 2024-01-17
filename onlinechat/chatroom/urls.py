from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path("add", views.add, name="add"),
    path('contacts/', views.contacts, name='contacts'),
    path('chat/<str:otherUser>/', views.chat, name='chat'),
    path('contactinfo/<str:username>', views.contactinfo, name='contactinfo'),
    path('changeusername', views.changeusername, name='changeusername'),
]