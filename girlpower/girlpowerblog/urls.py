from django.urls import path
from .views import Home, BlogDetails

urlpatterns = [
    # path('', views.home, name='home'),
    path('', Home.as_view(), name="home"),
    path('singleblog/<int:pk>', BlogDetails.as_view(), name="blogdetails" ),
]
