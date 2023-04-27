from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    # CharField is a string field
    title = models.CharField(unique=True, max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    # - ForeignKey is a relationship field (many-to-one),
    #   it means that one user can have many posts
    # - on_delete=models.CASCADE means that if the user is deleted,
    #   then all of their posts will be deleted as well
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    # auto_now means the date will be updated every time the post is updated
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    # - CloudinaryField is a field for storing images in Cloudinary
    # - default='placeholder' means if the image is not uploaded,
    #   then a placeholder will be displayed
    featured_image = CloudinaryField('image', default='placeholder')
    # blank=True means the field is not required when creating a post
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # choices means the user can only choose between Draft and Published
    status = models.IntegerField(choices=STATUS, default=0)
    # related_name='blog_likes' means that the user can access the posts
    # they liked by using the blog_likes attribute
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    # meta class is used to specify model-specific options
    class Meta:
        # the posts will be ordered by the date they were created
        # (the newest posts will be displayed first)
        # - means descending order
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        '''Returns the total number of likes for a post'''
        return self.likes.count()


class Comment(models.Model):
    # - ForeignKey is a relationship field (many-to-one),
    #   it means that one post can have many comments
    # - related_name specifies the name of the reverse relation from the
    #   User model back to your model.
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        # order the comments by the date they were created, ascending order
        # (the oldest comments will be listed first)
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
