from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):   # Creating the Post class for the blog
    '''
    Here we create the different field types for the database that are used
    to describe each blog post
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Creating the Author
    title = models.CharField(max_length=200)                                        # The blog post title
    text = models.TextField()                                                       # The text
    created_date = models.DateTimeField(default=timezone.now)                       # The datetime of post creation
    published_date = models.DateTimeField(blank=True, null=True)                    # The publish datetime

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title