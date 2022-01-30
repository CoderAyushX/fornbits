from django.shortcuts import render,redirect
from .models import Category,Post,blogpostComment

# Create your views here.
def blogs(request):
    cat = Category.objects.all()
    post = Post.objects.all()
    context = {
        'cats': cat,
        'posts':post
    }
    return render(request, 'blogs.html', context)

def blogpost(request, url):
    post =  Post.objects.get(url=url)
    relatedPost = Post.objects.all().exclude(post_id= post.post_id)[:5]
    #work to do here
    comments = blogpostComment.objects.filter(post = post)
    context = {
        'posts':post,
        'comment': comments,
        'relatedpost': relatedPost
    }
    return render(request, 'blogpost.html', context)

def category(request, url):
    searchCat = Category.objects.get(url = url)
    post =  Post.objects.filter(cat=searchCat)
    cat = Category.objects.all()
    context = {
        'cats': cat,
        'posts':post
    }
    return render(request, 'blogs.html', context)

def comment(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.method == "POST":
         comment = request.POST.get('comment')
         user = request.user
         postno  =  request.POST.get('Sno')
         post = Post.objects.get(post_id = postno)
         comment = blogpostComment(comments= comment, user= user, post= post)
         comment.save()
    return redirect(f'/blogs/{post.url}')