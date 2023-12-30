from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.IntegerField()
    img = models.CharField(max_length=45)
    
    def __str__(self):
        return self.first_name 

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=45)
    type_of_room = models.CharField(max_length=45)
    room_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.hotel_name 
    
    
class Package(models.Model):
    package_name = models.CharField(max_length=45)
    package_type = models.CharField(max_length=45)
    package_price = models.IntegerField()
    package_description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    package_duration = models.IntegerField()
    end_date = models.DateField()
    start_at = models.DateField()
    
    def __str__(self):
        return self.package_name 
    
    
class Event(models.Model):
    event_name = models.CharField(max_length=45)
    event_type = models.CharField(max_length=45)
    event_description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.event_name 

class PackageEvent(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE) 

class HotelPackages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE) 
    package = models.ForeignKey(Package, on_delete=models.CASCADE) 
    

class Bill(models.Model):
    amount = models.IntegerField()
    visa_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    
    
class Booking(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

class FeedBack(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
