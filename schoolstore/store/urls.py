
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('home/',views.home,name='home2'),
    path('loginn/',views.userlogin,name='login'),
    path('siginupp/',views.usersignup,name='signup'),
    path('newentry/',views.newentry,name='newwntry'),
    path('ajax/load-course/', views.load_course, name='ajax_load_course'),
]
