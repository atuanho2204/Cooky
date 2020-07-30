from django.urls import path
from .views import LoginClass, ViewUser
from . import views

urlpatterns = [
    path('index/foodcard/<int:id>/', views.food_card, name='food-card'),
    path('test/', views.food_menu, name='index'),
    path('food_card/', views.food_card, name='food-card'),
    path('login/', LoginClass.as_view(), name='login'),
    path('index/', views.food_menu, name='index'),
    path('signup/', views.signup, name='signup'),
    path('', views.logout_view, name='log-out'),
    path('404page', views.error, name='404page')
]