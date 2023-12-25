from collections.abc import Iterable
from django.db import models
from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile",null=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(upload_to="profile_pics",null=True,blank=True)
    DOB=models.DateField(null=False,blank=False)
    Bio=models.CharField(max_length=200,null=True,blank=False)
    following=models.ManyToManyField("self",related_name="followed_by",symmetrical=False,null=True)
    block=models.ManyToManyField("self",related_name="blocked",symmetrical=False,null=True)

    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse('profile-edit', kwargs={'pk': self.pk})
    
class Posts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_post")
    title=models.CharField(max_length=200)
    post_image=models.ImageField(upload_to="posters",null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    liked_by=models.ManyToManyField(User,related_name="post_like")

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    user=models.ForeignKey(User,related_name="comment",on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="post_comments")

    def __str__(self):
        return self.text
    
class Stories(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userstories")
    title=models.CharField(max_length=200)
    post_image=models.ImageField(upload_to="stories",null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    # exp=created_date+timezone.timedelta(days=1)
    expiry_date=models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.expiry_date:
            self.expiry_date=timezone.now()+timezone.timedelta(days=1)
        super().save(*args,**kwargs)





def created_profile(sender, created, instance, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("Profile object created for user:", instance.username)

post_save.connect(created_profile, sender=User)

