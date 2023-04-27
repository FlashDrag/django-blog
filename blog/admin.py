from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''
    Adds the summernote editor to the admin page for posts.

    Decorator registers the both Post model and PostAdmin class
    with our admin site, insead of registering it
    separately with admin.site.register()
    '''

    # summernote_fields with the name of the field
    # that we want to use the editor for
    summernote_fields = ('content')
