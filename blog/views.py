from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
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


# Post/Redirect/Get pattern
# PRG pattern used to prevent duplicate form submissions
# It means that after a POST request, we redirect to a GET request to the same
# page with messages and errors if any.
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

        # get only messages with the tag 'comment-alert'
        storage = messages.get_messages(request)
        comment_alerts = [message for message in storage
                          if 'comment-alert'
                          in (message.extra_tags, )]

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_alerts": comment_alerts,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        '''Handle POST request to create a new comment'''
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

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

            messages.success(request, 'Thank you for your comment!\n'
                             'Your comment is awaiting moderation.',
                             extra_tags='comment-alert')
        else:
            messages.error(request, 'Error adding your comment',
                           extra_tags='comment-alert')

        # reverse() allows us to look up the URL for a given view by its name
        # return HttpResponseRedirect(reverse('post_detail', args=[slug]))

        # redirect to the same page keeping the same scroll position
        # Note: keep in mind that history.back() does not 'reload' the page
        return HttpResponse('<script>history.back();</script>')


'''
class PostLikeToggle(RedirectView):
    # Toggle like/unlike for a post
    # with page refresh using with RedirectView
    # append the query string to the redirect URL
    query_string = True
    # define the name of the URL pattern to be redirected to
    pattern_name = "post_detail"

    def get_redirect_url(self, *args, **kwargs):
        slug = kwargs.get('slug')
        post = get_object_or_404(Post, slug=slug)

        # toggle like/unlike: remove/add the user to the post's likes list
        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(self.request.user)
        else:
            post.likes.add(self.request.user)

        # generate the redirect URL
        return super().get_redirect_url(*args, **kwargs)

class PostLikeToggle(View):
    # Toggle like/unlike for a post with post method
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
'''


class PostLikeToggle(View):
    '''
    Toggle like/unlike for a post with AJAX request
    without page refresh.
    The way is used insead redirectview and
    `HttpResponse('<script>history.back();</script>')`
    as I need to update number of likes without page refresh
    when user clicks on like/unlike button.
    '''

    def post(self, request, slug, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'result': 'error',
                                 'message': 'User not authenticated'})
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            result = 'unliked'
        else:
            post.likes.add(request.user)
            result = 'liked'
        like_count = post.number_of_likes()
        return JsonResponse({'result': 'success', 'action': result,
                             'like_count': like_count})
