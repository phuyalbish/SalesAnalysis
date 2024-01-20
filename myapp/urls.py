from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home_index, name='index'),
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard')
]