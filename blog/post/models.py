from django.db import models

import markdown2
# Create your models here.


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True, editable=False)
    edited_at = models.DateField(auto_now=True, editable=False)
    editor = models.TextField()
    content = models.TextField(editable=False)

    def save(self, *args, **kwargs):
        self.content = markdown2.markdown(str(self.editor))
        super(Post, self).save(*args, **kwargs)

