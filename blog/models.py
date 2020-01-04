from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title


    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Blog(models.Model):
    title  = models.CharField(max_length=100, unique=True)
    slug   = models.SlugField(max_length=100, unique=True)
    body   = models.TextField()
    photo  = models.ImageField(upload_to='blog_image/%Y/%m/%d/')
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s' % self.title


    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

