from django.urls import path
from .views import *
from . import views

urlpatterns = [path("", views.index, name="index"),
               path("UserLogin.html", views.UserLogin, name="UserLogin"),	      
               path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
               path('register/', UserRegisterAction, name='UserRegisterAction'),
               path('user-screen/', views.UserScreenView, name='UserScreen'),
	           path("LoadDataset", views.LoadDataset, name="LoadDataset"),	      
               path("FastText", views.FastText, name="FastText"),
               path("TrainML", views.TrainML, name="TrainML"),
               path("DetectFake.html", views.DetectFake, name="DetectFake"),
               path("DetectFakeAction", views.DetectFakeAction, name="DetectFakeAction"),    
               path('admin-login/', admin_login, name='admin_login'),  
               path('users/', list_users, name='list_users'),  
               path('users/delete/<int:user_id>/', delete_user, name='delete_user'),  
               path('admin-logout/', admin_logout, name='admin_logout'),          
]



