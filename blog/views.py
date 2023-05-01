from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm


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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        '''Handle POST request to create a new comment'''
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # set the comment's email and username automatically
            # from the logged in user
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username

            # create a new comment but don't commit(save) to the database yet
            new_comment = comment_form.save(commit=False)

            # assign the current post to the comment
            new_comment.post = post

            # save the comment to the database
            new_comment.save()

        else:
            # if the form is invalid, return an empty form instance
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form,
            },
        )
