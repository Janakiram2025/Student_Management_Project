# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('signup/', views.signup_select, name='signup-select'),
    path('signup/student/', views.signup_student, name='signup-student'),
    path('signup/teacher/', views.signup_teacher, name='signup-teacher'),
    #path('signup/teacher/', views.signup_teacher, name='signup-teacher'),
    path('signup/', views.signup_select, name='signup-select'),
    path('signup/student/', views.signup_student, name='signup-student'),
    path('login/student/', views.login_student, name='login-student'),
    path('login/teacher/', views.login_teacher, name='login-teacher'),
    #path('logout/', views.logout_user, name='logout'),
    path('login/teacher/', views.login_teacher, name='login-teacher'),
    path('login/admin/', views.login_admin, name='login-admin'),
    path('dashboard/admin/', views.admin_dashboard, name='admin-dashboard'),
    path('logout/', views.logout_view, name='logout'),



    # make sure you have this
]
