
from django.urls import include, path
from authen import views



app_name = "authen" #!

urlpatterns = [
  path("login_user/", views.loginUser, name="login"),
  path("logout_user/", views.logoutUser, name="logout"),
  path("register_user/", views.registerUser, name="register"),

]
