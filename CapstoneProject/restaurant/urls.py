


from django.contrib import admin 
from django.urls import path 
from rest_framework.authtoken.views import obtain_auth_token
from  .views import bookings,menues

  
urlpatterns = [ 
   
    path('api-token-auth',obtain_auth_token),
    path('menues',menues,name='menues'),
    path('bookings',bookings,name='bookings'),
   
   
]