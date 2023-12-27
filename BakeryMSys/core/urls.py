from django.urls import path
from core import views

urlpatterns = [
    path('', views.logIn, name='login'),
    path('home/', views.home, name='home'),
    path('add/', views.addOrder, name='add'),
    path('find/', views.findOrder, name='search'),
    path('update/', views.updateOrder, name='update'),
    path('admin/', views.AdminRedirect, name='admin'),
]