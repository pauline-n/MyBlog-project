from django.urls import path
from .views import Home, BlogDetails, AddPost, UpdatePost, DeletePost

urlpatterns = [
    
    path('', Home.as_view(), name="home"),
    path('singleblog/<int:pk>', BlogDetails.as_view(), name="blogdetails" ),
    path('addpost/', AddPost.as_view(), name="addpost"),
    path('singleblog/edit/<int:pk>', UpdatePost.as_view(), name="updatepost"),
    path('singleblog/<int:pk>/delete', DeletePost.as_view(), name="deletepost"),
]
