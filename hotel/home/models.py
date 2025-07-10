from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField( default = uuid.uuid4 , editable = False , primary_key = True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField( auto_now_add=True)
    
    class Meta:
        abstract = True
    
class Amenities(BaseModel):
    amenities_name = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.amenities_name
    
class Hotel(BaseModel):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)
    description = models.TextField()
    room_count = models.IntegerField(default = 10)
    
    def __str__(self):
        return self.hotel_name
            
class Hotel_Image(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="images")  # One-to-Many (Hotel → Images)
    image = models.ImageField(upload_to="hotel_images/")  # Stores images in media/hotel_images/

    def __str__(self):
        return f"Image for {self.hotel.hotel_name}"
    
class Hotel_Booking(BaseModel):
    hotel = models.ForeignKey(Hotel ,  on_delete=models.CASCADE, related_name = "hotel_booking")
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name = "user_booking")
    start_date = models.DateField()
    last_date = models.DateField()
    BOOKING_CHOICES = [
        ('Pre Paid', 'Pre Paid(Pay before stay)'),
        ('Post Paid', 'Post Paid(Pay after stay)'),
    ]
    booking_type = models.CharField(max_length=20, choices=BOOKING_CHOICES)  # Fixed choices and added max_length


   