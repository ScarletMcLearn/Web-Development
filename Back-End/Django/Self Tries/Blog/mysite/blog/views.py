from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .models import *

from django.shortcuts import render, redirect

from django.http.response import Http404

from .forms import * 

from django.urls import reverse



# Get QuerySet of Posts by Tag Str lists
def get_posts_by_tags(str_tag_list):
    return Post.objects.filter(tags__name__in=str_tag_list).distinct()


def index(request):
    latest_post_list = Post.objects.order_by('-published_date')[:5]
    # output = ', '.join([p.title for p in latest_post_list])

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.title = request.POST['title']
            post.body = request.POST['body']

            post.save()
            form.save_m2m()

            # form = PostForm()

            # print(request.POST['title'])
            # return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()


    context = {'latest_posts':latest_post_list, 'form':form, }
    return render(request, 'blog/index.html', context)

def add(request):
    return HttpResponse("Hello, world. You're at the blog add post page.")


def detail(request, slug):
    try:
        post = get_object_or_404(Post, slug = slug.lower())
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    comments = []

    try:
         comments_list = post.comment_set.all()
         
         for c in comments_list:
            comments.append(c)

        

    except Http404:
         pass
 


    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)
            comment.post = post
            comment.body = request.POST['body']

            comment.save()

            # form = PostForm()

            # print(request.POST['title'])
            # return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    

    


    return render(request, "blog/detail.html", {"post": post, 'comments':comments, 'form':form})








def edit(request, slug):
    try:
        post = get_object_or_404(Post, slug = slug.lower())
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            temp_post = form.save(commit=False)
            temp_post.title = request.POST['title']
            temp_post.body = request.POST['body']
            post.delete()
            temp_post.save()
            form.save_m2m()

            # form = PostForm()

            # print(request.POST['title'])
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        form = PostForm(instance=post)


    context = {
        # 'latest_posts':latest_post_list, 
        'form':form, }
    return render(request, 'blog/forms/add_post.html', context)