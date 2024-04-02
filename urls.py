from django.contrib import admin
from django.urls import path
from commit import views

urlpatterns = [
    path('', views.login_page, name='login'),  # Assuming 'cenima_read' is your home view
    path('create/', views.cenima_create, name='createmovie'),
    path('read/', views.cenima_read, name='readmovie'),
    path('update/<int:pk>/', views.cenima_update, name='update'),
    path('delete/<int:pk>/', views.cenima_delete, name='delete'),
    path('',views.login_page,name='home'),
    path('signup/',views.signup_page,name='signup'),
    path('logout/', views.logout_view,name='logout'),
    path('aboutUs/', views.aboutUs,name='aboutus'),
]
