from django.urls import path
from . import views

urlpatterns = [
    # path("",views.home, name="home"),
    #  path("contact",views.contact_view, name="contact_view"),
    #  path("login_view/",views.login_view, name="login_view"),
     path("",views.home, name="home"),
     path("signup/",views.signup, name="signup"),
     path('user_login/', views.user_login, name='user_login')
,
    

]