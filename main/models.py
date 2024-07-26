from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    category=models.OneToOneField(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image/course/', null=True,  blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.CharField(max_length=255)
    data_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    image=models.ImageField(upload_to='image/blog/', null=True, blank=True)
    content = models.TextField()
    data_created = models.DateTimeField(default=timezone.now)
    
    

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    message = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50]

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
    
    
