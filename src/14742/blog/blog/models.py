from django.db import models


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
            # or self.__dict__[field.name]
        kwargs.pop('id')
        if "date_created" in kwargs.keys():
            kwargs.pop("date_created")

        new_instance = self.__class__(**kwargs)
        new_instance.save()

        return new_instance.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, db_constraint=True)
    text = models.TextField(max_length=500)
