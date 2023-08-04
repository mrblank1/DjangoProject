from django.db import models

# Create your models here.
class Post(models.Model):
    #author
    title = models.CharField(max_length=255)
    content=models.TextField(max_length=255)
    #image
    #tags
    #category
    counted_views = models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    create_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_at=models.DateTimeField(null=True)
    class Meta:
        ordering= ('create_date',)
    def __str__(self):
        return self.title