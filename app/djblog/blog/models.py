""" Blog models """

import datetime
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify


def gen_slug(s):
    """ Genirate slug with transliteration """
    transliteration = {'а': 'a', 'б': 'b', 'в': 'v',
                       'г': 'g', 'д': 'd', 'е': 'e', 
                       'ё': 'yo', 'ж': 'zh', 'з': 'z', 
                       'и': 'i', 'й': 'j', 'к': 'k', 
                       'л': 'l', 'м': 'm', 'н': 'n', 
                       'о': 'o', 'п': 'p', 'р': 'r', 
                       'с': 's', 'т': 't', 'у': 'u', 
                       'ф': 'f', 'х': 'kh', 'ц': 'ts', 
                       'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 
                       'ы': 'i', 'э': 'e', 'ю': 'yu','я': 'ya'}
    new_slug = slugify(''.join(transliteration.get(w, w) for w in s.lower()))
    created_time = (datetime.datetime.now()).strftime('%d-%m-%Y_%H-%M-%S')
    return f'{new_slug}-created-{created_time}'


class Post(models.Model):
    """ Posts model """
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_pub = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        """ Reverse post detail """
        return reverse("post_detail_url", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']


class Tag(models.Model):
    """ Tags model """
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """ Reverse tag detail """
        return reverse("tag_detail_url", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_create']
