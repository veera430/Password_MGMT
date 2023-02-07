from django.urls import path
from .views import ArticleViewset
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('reset_pass/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_pass_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_pass_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]