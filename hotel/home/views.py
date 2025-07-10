from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth  import authenticate , login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import (Amenities , Hotel , Hotel_Booking)
from django.db.models import Q , Count

# Create your views here.

    
def home(request):
    amenities_objs = Amenities.objects.all()
    hotels_objs = Hotel.objects.all()

    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    amenities = request.GET.getlist('amenities')
    print(amenities)
    if sort_by:
        if sort_by == 'ASC':
            hotels_objs = hotels_objs.order_by('hotel_price')
        elif sort_by == 'DSC':
            hotels_objs = hotels_objs.order_by('-hotel_price')

    
    if search:
        hotels_objs = hotels_objs.filter(Q(hotel_name__icontains = search) | Q(description__icontains = search) )
         
    if amenities:
        hotels_objs = hotels_objs.filter(amenities__amenities_name__in=amenities) \
            .annotate(matching_amenities=Count('amenities', filter=Q(amenities__amenities_name__in=amenities))) \
            .filter(matching_amenities=len(amenities))




    context = {'amenities_objs' : amenities_objs , 'hotels_objs' : hotels_objs , 'sort_by' : sort_by 
    , 'search' : search , 'amenities' : amenities}
    return render(request , 'home.html' ,context)


def login_page(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username)
        
        if not user_obj.exists():
            
           messages.warning(request, "account not found")
           return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Redirects the user back to the previous page
       
        user_obj = authenticate(username =  username , password = password)
        if not user_obj:
              messages.warning(request, "Invalid Credentials")
              return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Redirect back
        
        # If authentication successful, log in the user
              
        login(request , user_obj)
            
        return redirect('/')
     return render(request , 'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = username)
        
        if user_obj.exists():
            
           messages.warning(request, "Username already exists")
           return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Redirects the user back to the previous page
       
        user = User.objects.create(username = username)
        user.set_password(password)
        user.save()
        return redirect('/')
    return render(request , 'register.html')
 
 
def check_booking(start_date  , last_date ,uid , room_count):
    qs = Hotel_Booking.objects.filter(
        start_date__lte=start_date,
        last_date__gte=last_date,
        hotel__uid = uid
        )
    
    if len(qs) >= room_count:
        return False
    
    return True
 
def hotel_detail(request,uid):
    hotel_obj = Hotel.objects.get(uid = uid)

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        hotel = Hotel.objects.get(uid = uid)
        if not check_booking(checkin ,checkout  , uid , hotel.room_count):
            messages.warning(request, 'Hotel is already booked in these dates ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        Hotel_Booking.objects.create(hotel=hotel , user = request.user , start_date=checkin
        , last_date = checkout , booking_type  = 'Pre Paid')
        
        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        

        
    
    return render(request , 'hotel_detail.html' ,{
        'hotels_obj' :hotel_obj
    })
    
def booked_rooms(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    search = request.GET.get('search', '')
    bookings = Hotel_Booking.objects.filter(user=request.user)
    if search:
        bookings = bookings.filter(hotel__hotel_name__icontains=search)
    return render(request, 'booked_rooms.html', {
        'bookings': bookings
    })

def logout_page(request):
    logout(request)
    return redirect('login_page')
    