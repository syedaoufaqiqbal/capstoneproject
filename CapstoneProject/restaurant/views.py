from .serializers import BookingSerializer, MenuSerializer
from .models import Booking
from .models import Menu
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
 


""" class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer """
""" class BookingView(ViewSet):
    def list(self, request):
      return Response({"message":"All bookings"}, status.HTTP_200_OK)
    def create(self, request):
      return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
    def update(self, request, id=None):
     return Response({"message":"Updating a book"}, status.HTTP_200_OK)
    def retrieve(self, request, id=None):
     return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
    def partial_update(self, request, id=None):
     return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
    def destroy(self, request, id=None):
      return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
   """
""" class MenuView(generics.ListCreateAPIView):
     queryset = Menu.objects.all()
     serializer_class = MenuSerializer """

def menues(request):
    return render(request, 'index.html', {'menues': Menu.objects.all()})	
def bookings(request):
    return render(request, 'index.html', {'bookings': Booking.objects.all()})  

""" class MenuView(ViewSet):
    def list(self, request):
      return Response({"message":"All menues"}, status.HTTP_200_OK)
    def create(self, request):
      return Response({"message":"Creating a menu"}, status.HTTP_201_CREATED)
    def update(self, request, id=None):
     return Response({"message":"Updating a menu"}, status.HTTP_200_OK)
    def retrieve(self, request, id=None):
     return Response({"message":"Displaying a menu"}, status.HTTP_200_OK)
    def partial_update(self, request, id=None):
     return Response({"message":"Partially updating a menu"}, status.HTTP_200_OK)
    def destroy(self, request, id=None):
      return Response({"message":"Deleting a menu"}, status.HTTP_200_OK) """