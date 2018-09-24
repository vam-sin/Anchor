from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class News(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/',default='')
    icon=models.ImageField(upload_to='images/',default='')
    votes_total=models.IntegerField(default=1)
    sailor=models.ForeignKey(User,on_delete=models.CASCADE)
    def pub_date_mod(self):
        return self.pub_date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]


class Comment(models.Model):
    post = models.ForeignKey('news.News', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
