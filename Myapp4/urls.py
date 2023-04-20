from django.contrib import admin
from django.urls import path
from Myapp4 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register,name='register'),
    path('login/',views.register,name='login'),
    path('home/',views.register,name='home'),
]
