from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('success/', views.success, name='success'),
   path('failure/', views.failure, name='failure'),

   path('register/', views.register, name='register'),
   # path('register2/', views.register2, name='register2'),
=======
 
]