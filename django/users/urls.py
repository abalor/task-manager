from django.urls import path
from .views import MyLoginView, RegisterView, MyProfile
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import(
    LogoutView ,
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView)
from . import views


urlpatterns = [
    # path('login/', MyLoginView.as_view(template_name = 'users/login.html'), name='login'),
    # path('register/', views.register, name='register'),
    # path('task_list/', views.task_list, name='task_list'),
    # path('home/', views.CreateTaskView.as_view(), name='CreateTaskView'),
    # path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    # path('', views.start_page, name='start_page'),


     
    path('login/', MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
    path('password-reset/', 
     PasswordResetView.as_view(
        template_name='users/password_reset.html',
        html_email_template_name='users/password_reset_email.html'
    ),
    name='password-reset'
), 
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    
    path('profile/', MyProfile.as_view(), name='profile'),

]
 