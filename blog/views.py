from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import  timezone
def blog_view(request):
    post_id=2
    increment_view_count(post_id)
    post=Post.objects.get(id=post_id)
    context={'post':post.counted_views}
    return render(request, 'blog/blog-home.html',context)
# I want to show the views in the blog-single
def blog_single(request):
    post_id=1
    increment_view_count(post_id)
    post=Post.objects.get(id=post_id)
    context={'post':post.counted_views}
    return  render(request, 'blog/blog-single.html',context)
# Create your views here.
# in the test I tried to call it
def blog_test(request):
    now = timezone.now()
    published_posts = Post.objects.filter(published_at__lte=now)

    context = {'posts': published_posts}
    return render(request, 'blog/test.html',context)
# I created a function which add a number to the counted_views of the the first post
def increment_view_count(post_id):
    
    post=Post.objects.get(id=post_id)
    post.counted_views+=1
    post.save()



