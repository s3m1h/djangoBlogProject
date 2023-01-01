from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
class Post(models.Model):
    ACTIVE = 'aktif'
    DRAFT = 'taslak'

    CHOICES_STATUS = (
        (ACTIVE, 'Aktif')
        (DRAFT, 'Taslak')
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)

    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.title