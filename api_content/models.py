from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    sort_order = models.IntegerField()

    def __str__(self):
        return self.title


class Block(models.Model):
    title = models.CharField(max_length=100)
    video_link = models.CharField(max_length=200)
    sort_order = models.IntegerField()
    view_count = models.IntegerField(default=0)
    pages = models.ManyToManyField(Page, related_name='blocks')

    def __str__(self):
        return self.title

    def increment_view_count(self):
        self.view_count += 1
        self.save()



