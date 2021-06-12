from django.db import models
from django.db.models.deletion import Collector


class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.TextField(max_length=250)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def copy(self):
        kwargs = {}
        for field in self._meta.fields:
            kwargs[field.name] = getattr(self, field.name)
        kwargs.pop('id')
        if "date_created" in kwargs.keys():
            kwargs.pop("date_created")

        new_instance = self.__class__(**kwargs)
        new_instance.save()
        if "comment_set" in dir(self):
            comments = self.comment_set.model.objects.filter(blog_post=self)
            for comments in comments:
                self.comment_set.model.objects.create(text=comments.text, blog_post=new_instance)
        return new_instance.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
