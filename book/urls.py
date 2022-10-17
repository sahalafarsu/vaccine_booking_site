
from .import views
from django.urls import path

# app_name='shopapp'
urlpatterns =[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('booking',views.booking,name='booking'),
    path('<slug:d_slug>/',views.booking,name='centers_by_district'),
    path('<slug:d_slug>/<slug:center_slug>/',views.centDetail,name='centDistdetail'),
    path('bookingslot',views.bookingslot,name='bookingslot'),
    path('success', views.success, name='success'),

]