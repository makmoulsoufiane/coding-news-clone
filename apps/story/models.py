from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    number_of_votes = models.IntegerField(default=1)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['-created_at']  # Order stories by creation date, newest first


class Vote(models.Model):
    story = models.ForeignKey(Story, related_name='votes', on_delete=models.CASCADE)

    created_by = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Increment the story's vote count when a new vote is created
        self.story.number_of_votes += 1
        self.story.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Vote by {self.user.username} for {self.story.title}'
