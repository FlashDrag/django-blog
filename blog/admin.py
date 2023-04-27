from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# SummernoteModelAdmin is a subclass of ModelAdmin.
# admin.ModelAdmin allows us to customize how our models
# are displayed in the admin panel.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''
    Adds the summernote editor to the admin page for posts.

    Decorator registers the both Post model and PostAdmin class
    with our admin site, insead of registering it
    separately with admin.site.register()
    '''

    # automatically generate the slug field from the title
    # e.g. title is 'My first post', then slug will be 'my-first-post'
    # It useful when we want to use the slug in the URL
    prepopulated_fields = {'slug': ('title',)}

    # list_filter adds a sidebar that allows us to filter posts
    # by status or created_on
    list_filter = ('status', 'created_on')

    # list_display adds columns to the post list page
    # so we can see the title, author, status and created_on
    list_display = ('title', 'author', 'status', 'created_on')

    # search_fields adds a search bar at the top of the post list page
    # so we can search for posts by title or content
    search_fields = ['title', 'content']

    # summernote_fields includes the fields of our model
    # that we want to use the editor for
    summernote_fields = ('content')
