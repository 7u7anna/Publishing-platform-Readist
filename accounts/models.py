from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150, null=False)
    date_joined = models.DateTimeField(auto_now=True)
    img = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"
