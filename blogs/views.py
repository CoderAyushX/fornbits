from django.shortcuts import render, redirect
from django.test import tag
from .models import Categorys, Posts, blogpostComments

# Create your views here.


def blogs(request):
    cat = Categorys.objects.all()
    post = Posts.objects.all().order_by("-upload_time")[:20]
    context = {
        'cats': cat,
        'posts': post
    }
    return render(request, 'blogs.html', context)


def blogpost(request, url):
    try:
        post = Posts.objects.get(url=url)
        relatedPost = Posts.objects.all().exclude(post_id=post.post_id)[:5]
        # work to do here
        comments = blogpostComments.objects.filter(post=post)
        def spaceRemove(text):
            TEXT = text.replace(" ", "")
            return TEXT
        tags = post.tags
        splitedText = tags.split(",")
        hastags = []
        for j in splitedText:
            hastags.append(spaceRemove(j))

        final = map(lambda x: f"#{x}", hastags)
        finalTags = list(final)
        context = {
            'posts': post,
            'comment': comments,
            'relatedpost': relatedPost,
            'tags': finalTags
        }
        return render(request, 'blogpost.html', context)
    except:
        return render(request, '500.html')


def category(request, url):
    searchCat = Categorys.objects.get(url=url)
    post = Posts.objects.filter(cat=searchCat)
    cat = Categorys.objects.all()
    context = {
        'cats': cat,
        'posts': post
    }
    return render(request, 'blogs.html', context)


def comment(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postno = request.POST.get('Sno')
        post = Posts.objects.get(post_id=postno)
        comment = blogpostComments(comments=comment, user=user, post=post)
        comment.save()
    return redirect(f'/blogs/{post.url}')
