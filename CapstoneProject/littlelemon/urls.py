from django.contrib import admin 
from django.urls import path ,include

urlpatterns = [ 
  path('admin/', admin.site.urls),
  path('restaurant/',include('restaurant.urls')),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.authtoken')), 

   # path('restaurant/', include('restaurant.urls')),
   # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) ,
   # path('auth/', include('djoser.urls')),
   # path('auth/', include('djoser.urls.authtoken')),
]
