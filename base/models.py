from secrets import choice
from django.db import models
from django.contrib.auth.models import User

primar_categories = (
    ('Finance', 'Finance'),
    ('Investing', 'Investing'),
    ('Sport', 'Sport'),
    ('Lifestyle', 'Lifestyle'),
    ('Technology', 'Technology'),
    ('Art', 'Art'),
    ('Health', 'Health'),
    ('Business', 'Business'),
    ('Literature', 'Literature'),
    ('History', 'History'),
    ('Culinaries', 'Culinaries'),
)

class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    sub_category = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, choices=primar_categories, null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



