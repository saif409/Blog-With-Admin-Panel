from django.db import models

# Create your models here.

class Author(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    profile_picture = models.ImageField(null=True,blank=True)
    country = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    present_address = models.CharField(max_length=200)
    permanent_address = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    article_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    article_pic = models.FileField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    post_comment = models.TextField()

    def __str__(self):
        return self.post.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
