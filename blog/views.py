from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    # Retrieve only published posts(STATUS=Published)
    # in descending order by created_on field
    # (using ordering option in model Meta class)
    queryset = Post.objects.filter(status=1)
    template_name = 'post_list.html'
    # Limit the number of posts per page to 6.
    # So, if the number of posts is greater than 6,
    # then django will automatically create pagination links
    paginated_by = 6
