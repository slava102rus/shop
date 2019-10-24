from .views import index,my_login,my_logout,my_register
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('login/',my_login,name='login'),
    path('logout/',my_logout,name="logout"),
    path('register/',my_register,name="register"),
]
