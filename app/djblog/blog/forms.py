""" Blog forms """

from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Tag



class TagForm(forms.ModelForm):
    """ Tag form """
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})
        }

    def clean_slug(self):
        """ Slug validation """
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug не можеть быть create')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug с именем "{new_slug}" уже существует!')
        return new_slug


class PostForm(forms.ModelForm):
    """ Post form """
    class Meta:
        model = Post
        fields =['title', 'slug', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ''}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': ''})
        }

    def clean_slug(self):
        """ Slug validation """
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug не можеть быть create')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug с именем "{new_slug}" уже существует!')
        return new_slug
