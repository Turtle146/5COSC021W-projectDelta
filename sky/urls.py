from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('organisation/', views.organisation_view, name='organisation'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:department_id>/', views.department_detail, name='department_detail'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='sky/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]