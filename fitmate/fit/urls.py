from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login_view, name = 'login'),
    path('register/', views.register_view, name='register'),
    path('password_reset/', view.password_reset_view, name= 'password_reset'),
]

