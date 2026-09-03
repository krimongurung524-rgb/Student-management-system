from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('search/', views.student_search, name='student_search'),
    path('<slug:slug>/', views.student_detail, name='student_detail'),
    path('<slug:slug>/edit/', views.student_update, name='student_update'),
    path('<slug:slug>/delete/', views.student_delete, name='student_delete'),
    path('<slug:slug>/profile/', views.student_profile, name='student_profile'),
]