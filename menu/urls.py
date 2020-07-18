from django.urls import path
from .views import LoginClass, ViewUser
from . import views

urlpatterns = [

    path('login/', LoginClass.as_view(), name='login'),
    path('', LoginClass.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.logout_view, name='log-out'),
]