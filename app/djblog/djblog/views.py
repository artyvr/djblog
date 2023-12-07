""" DJBlog views """

from django.shortcuts import redirect


def redirect_blog(request):
    """ Redirect to blog """
    return redirect('posts_list_url', permanent=True)
