from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_init, post_save
from django.dispatch import receiver

from taggit.managers import TaggableManager
# Create your models here.


# class User(User):
#     pass


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    image = models.ImageField(default='default.jpg',
                              upload_to='../media/profile_photo')

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()


class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=1, max_digits=1, default=0.0)
    tags = TaggableManager()
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0.00)
    # image = models.ImageField(default='default.jpg',
    #   upload_to='../media/ad_photo')
    # images = models.ManyToManyField(Image)

    def __str__(self):
        return self.title + self.content


class Image(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='../media/ad_photo')


class Comment(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
