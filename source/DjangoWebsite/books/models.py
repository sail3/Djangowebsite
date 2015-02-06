from django.db import models

class Publisher(models.Model):
    name = models.CharField(maxlength = 30)
    address = models.CharField(maxlength = 50)
    city = models.CharField(maxLength = 30)
    state_province = models.CharField(maxLength = 30)
    country = models.CharField(maxLength = 50)
    website = models.URLField()
    def __str__(self):
        return self.name

class Author(models.Model):
    salutation = models.CharField(maxLength = 10)
    first_name = models.CharField(maxLength = 30)
    last_name = models.CharField(maxLength = 40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to = '/tmp')
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(maxLength = 100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    def __str__(self):
        return self.title
