from django.urls import path
from main import views


urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('course/', views.course, name="course"),
    path('about/', views.about, name="about"),
    path('blog-single/', views.BlogSingle, name="blog-single"),
    path('blog/', views.blog, name="blog"),
    path('course-single/<int:id>', views.CourseSingle, name="course-single"),
    path('search-page/', views.SearchPage, name="search-page"),
    path('search-none/', views.SearchNone, name="search-none"),
    
    
    
    
    
    
    
    
]
