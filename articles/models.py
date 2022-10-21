from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Review(models.Model):
  genre_choice = (
    ('Action', 'Action'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Fantasy', 'Fantasy'),
    ('Horror', 'Horror'),
    ('Mystery', 'Mystery'),
    ('Romance', 'Romance'),
    ('Thriller', 'Thriller'),
    ('Sci-fi', 'Sci-fi'),
    ('Others', 'Others'),
  )

  title = models.CharField(max_length=50)
  content = models.TextField()
  movie_name = models.CharField(max_length=50)
  grade = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  genre = models.CharField(max_length=50, choices=genre_choice)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/movies', default='no_img.png')
  image_thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(295, 295)],
                                format='JPEG',
                                options={'quality': 80})

class Comment(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  review = models.ForeignKey(Review, on_delete=models.CASCADE)