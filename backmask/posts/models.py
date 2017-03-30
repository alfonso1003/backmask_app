from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/images', default=None)
    audio = models.FileField(upload_to='media/audio', default=None)
    # reversed_audio = 
    body = models.TextField()
    
    def __str__(self):
        return self.title
        
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
        
    def summary(self):
        return self.body[:100] + '...'