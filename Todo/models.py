from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        blank = True,
        null = True,
    )

    def get_followings(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()

    def get_absolute_url(self):
        return reverse("user_profile", args=[str(self.id)])

    def __str__(self):
            return self.username

class UserConnection(models.Model):
    creator = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="creators"
    )
    following = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name="followings"
    )

    def __str__(self):
        return self.creator.username + ' Follows ' + self.following.username

class Todolist(models.Model):
    title = models.TextField(blank=True, null=True)
    finish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("list_detail", args=[str(self.id)])



