from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('student/', views.Students_mainpage, name='surn'),
    path('Students/<int:student_id>/', views.student_index, name='students_id'),
    path('client_err_test/', views.err_400),
    path('server_err_test/', views.err_500),
]

