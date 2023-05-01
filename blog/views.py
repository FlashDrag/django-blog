from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    # Retrieve only published posts(STATUS=Published)
    # in descending order by created_on field
    # (using ordering option in model Meta class)
    queryset = Post.objects.filter(status=1)
    template_name = 'index.html'
    # Limit the number of posts per page to 6.
    # So, if the number of posts is greater than 6,
    # then django will automatically create pagination links
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        '''Retrieve a post by slug'''
        # get only published posts(STATUS=Published)
        queryset = Post.objects.filter(status=1)
        # shortcut to get the post by slug or return 404
        # if the post is not found
        post = get_object_or_404(queryset, slug=slug)
        # get approved comments for this post ordered by ascending date
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        # if the user has liked the post, then set liked to True
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
