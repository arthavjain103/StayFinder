from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
   path('' , home , name = "home"),
   path('check_booking/' , check_booking),
   path('login/' , login_page , name = 'login_page'),
   path('register/' , register_page , name = 'register_page'),
   path('hotel_detail/<uuid:uid>/', hotel_detail, name='hotel_detail'),
   path('booked-rooms/', booked_rooms, name="booked_rooms"),
   path('logout/', views.logout_page, name='logout_page'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()