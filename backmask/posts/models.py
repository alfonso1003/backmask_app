from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/images', default=None)
    audio = models.FileField(upload_to='media/audio', default=None)
    body = models.TextField()
    
    def __str__(self):
        return self.title
        
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
        
    def summary(self):
        return self.body[:100] + '...'

    def reverse_audio(self):
        # TODO: give backwards file a unique name
        # TODO: properly define outfile
        # TODO: make reversed audio a class attribute
        outfile = '../media/audio/backwards.wav'
        try:
            if self.audio.endswith('.wav'):
                os.system('sox %s %s reverse' % (self.audio, outfile) )
            else:
                os.system('lame --decode %s - | sox - %s' % (self.audio, outfile) ) 
        except:
            outfile = self.audio
        
        return outfile