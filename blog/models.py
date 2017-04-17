from django.db import models

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Entry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media',default='No image')
    perex = models.TextField(max_length=2000,default='Oops Nothing here!!')
    content = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Blog"
        verbose_name_plural= "Blogs"
        ordering = ["-created"]

    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'slug': self.slug})