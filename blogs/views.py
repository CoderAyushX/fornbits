from django.shortcuts import render, redirect
from django.test import tag
from .models import Category, Post, blogpostComment

# Create your views here.


def blogs(request):
    cat = Category.objects.all()
    post = Post.objects.all()
    context = {
        'cats': cat,
        'posts': post
    }
    return render(request, 'blogs.html', context)


def blogpost(request, url):
    try:
        post = Post.objects.get(url=url)
        relatedPost = Post.objects.all().exclude(post_id=post.post_id)[:5]
        # work to do here
        comments = blogpostComment.objects.filter(post=post)
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
    searchCat = Category.objects.get(url=url)
    post = Post.objects.filter(cat=searchCat)
    cat = Category.objects.all()
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
        post = Post.objects.get(post_id=postno)
        comment = blogpostComment(comments=comment, user=user, post=post)
        comment.save()
    return redirect(f'/blogs/{post.url}')
