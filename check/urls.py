from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
# from .views import UserPostListView


urlpatterns = [
    path('',views.question,name='personality-form'),
    path('register/', views.register, name="user-registration"),
    path('profile',views.UserRes, name = 'user-profile'),
    path('UpdateProfile/', views.profile, name="user-updateprofile"),
    path('login/',auth_views.LoginView.as_view(template_name='check/login.html'), name="user-login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='check/logout.html'), name="user-logout"),
    path('description/',views.description,name="desc"),
    path('about/',views.about,name="about")
]
