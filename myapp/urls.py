from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home_index, name='index'),
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('charts/', views.charts_view, name='charts'),
    path('tables/', views.tables_view, name='tables'),


    path('company/', views.company, name='company'),

    
    path('create_company/', views.create_company, name='create_company'),
]