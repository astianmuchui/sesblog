from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.POST:
        try:
            post = models.Post(
                title=request.POST['title'],
                author=request.POST['author'],
                content=request.POST['content']
            )
            post.save()
            return HttpResponseRedirect('/all')
        except Exception as e:
            print(f"Error creating post: {e}")
    return render(request, 'posts/create.html')

def all(request):
    try:
        posts = models.Post.objects.all().order_by('-created_at')
    except Exception as e:
        print(f"Error fetching posts: {e}")
        posts = []
    ctx = {
        'posts': posts
    }
    return render(request, 'posts/all.html', ctx)

def view(request, id):
    try:
        post = models.Post.objects.get(id=id)
    except models.Post.DoesNotExist:
        print(f"Post with id {id} does not exist.")
        post = None
    except Exception as e:
        print(f"Error fetching post: {e}")
        post = None
    ctx = {
        'post': post
    }
    return render(request, 'posts/view.html', ctx)

def edit(request, id):
    try:
        post = models.Post.objects.get(id=id)
    except models.Post.DoesNotExist:
        print(f"Post with id {id} does not exist.")
        return HttpResponseRedirect('/all')
    except Exception as e:
        print(f"Error fetching post: {e}")
        return HttpResponseRedirect('/all')

    ctx = {
        'post': post
    }

    if request.POST:
        try:
            post.title = request.POST['title']
            post.author = request.POST['author']
            post.content = request.POST['content']
            post.save()
            return HttpResponseRedirect('/all')
        except Exception as e:
            print(f"Error updating post: {e}")

    return render(request, 'posts/edit.html', ctx)

def delete(request, id):
    try:
        post = models.Post.objects.get(id=id)
        post.delete()
    except models.Post.DoesNotExist:
        print(f"Post with id {id} does not exist.")
    except Exception as e:
        print(f"Error deleting post: {e}")
    return HttpResponseRedirect('/all')
