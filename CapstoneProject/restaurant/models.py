from django.db import models

class Booking(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField( ) 
    bookingdate=models.DateTimeField()
    class Meta:
        indexes = [
            models.Index(fields=['id']),
        ]
    def __str__(self):
      return self.name    
        
        
class Menu(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
def __str__(self):
      return self.title  