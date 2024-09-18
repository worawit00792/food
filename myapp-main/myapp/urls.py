
from django.contrib import admin
from django.urls import path
from .views import index,p1,p2,p3,profile

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('p1/',p1, name='p1'),
    path('p2/',p2, name='p2'),
    path('p3/',p3, name='p3'),
    path('profile/',profile, name='profile'),
]
