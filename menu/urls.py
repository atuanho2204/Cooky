from django.urls import path
from .views import LoginClass, ViewUser
from . import views

urlpatterns = [
    path('test/', views.food_menu, name='index'),
    path('food_card/', views.food_card, name='food-card'),
    path('login/', LoginClass.as_view(), name='login'),
    path('', LoginClass.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.logout_view, name='log-out'),
]