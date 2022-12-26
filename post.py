from django.db import models

from fb_post.models.user import User


class Post(models.Model):
    description = models.CharField(max_length=213)
    pub_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="posts")

    def __str__(self):
        return self.description
