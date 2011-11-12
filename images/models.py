from django.db import models
from datetime import datetime
import settings
from os.path import splitext


class Tag(models.Model):
    label = models.CharField(max_length=200)

    def __unicode__(self):
        return self.label
    

class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    filename = models.CharField(max_length=200)
    publication_date = models.DateField(default=datetime.now)
    tags = models.ManyToManyField(Tag, through="Tagging")

    def __unicode__(self):
        return self.title

    def image_url(self):
        return settings.MEDIA_URL + self.filename

    def thumb_url(self):
        (base, extension) = splitext(self.filename)
        return settings.MEDIA_URL + base + "_thumbnail" + extension


class Tagging(models.Model):
    tag = models.ForeignKey(Tag)
    image = models.ForeignKey(Image)

    def __unicode__(self):
        return "'%s' on image '%s'" % (self.tag, self.image.title)

