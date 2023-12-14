""" Blog utils """

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.cache import cache
from django.conf import settings
from .models import Post, Tag


class ObjectDetailMixin:
    """ Detail object mixin class """
    model = None
    template = None

    def get(self, request, slug):
        """ Get request """
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request,
                      self.template,
                      {self.model.__name__.lower(): obj, 'admin': obj, 'detail': True}
                      )


class ObjectCreateMixin:
    """ Create object mixin class """
    form_model = None
    template = None

    def get(self, request):
        """ Get request """
        form = self.form_model()
        return render(request, self.template, {'form': form})

    def post(self, request):
        """ Post request """
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            bound_form.instance.user = request.user
            new_obj = bound_form.save()
            cache.delete(settings.POSTS_CACHE_NAME)
            return redirect(new_obj)
        return render(request, self.template, {'form': bound_form})


class ObjectUpdateMixin:
    """ Object update mixin """
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        """ Get request """
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render (request,
                       self.template,
                       {'form': bound_form, self.model.__name__.lower(): obj}
                       )

    def post(self, request, slug):
        """ Post request """
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)
        if bound_form.is_valid():
            bound_form.instance.user = request.user
            new_obj = bound_form.save()
            cache.delete(settings.POSTS_CACHE_NAME)
            return redirect(new_obj)
        return render (request,
                       self.template,
                       {'form': bound_form, self.model.__name__.lower(): obj}
                       )


class ObjectDeleteMixin:
    """ Object delete mixin """
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        """ Get request """
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, {self.model.__name__.lower(): obj})

    def post(self, request, slug):
        """ Post request """
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        cache.delete(settings.POSTS_CACHE_NAME)
        return redirect(reverse(self.redirect_url))
