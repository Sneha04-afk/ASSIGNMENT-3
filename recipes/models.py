from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    recipe_img = models.ImageField(upload_to="recipe_images")
    total_time = models.CharField(max_length=20)
    servings = models.PositiveIntegerField()

    def __str__(self):
        return self.recipe_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.recipe_img.path)

        if img.height > 500 or img.width > 650:
            output_size = (500, 650)
            img.thumbnail(output_size)
            img.save(self.recipe_img.path)
    
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})