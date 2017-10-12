from django.db import models


# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name', 'last_name']


class BookManager(models.Manager):
    def title_count(self, keyword):
        # returns the number of books that title contains the given keyword
        return self.filter(title__icontains=keyword).count()


class AlbertBookManager(models.Manager):
    def get_queryset(self):
        return super(AlbertBookManager,
                     self).get_queryset().filter(authors__last_name__contains='Einstein')


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    objects = BookManager()
    albert_objects = AlbertBookManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
