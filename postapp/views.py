from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # ファイルを処理するために request.FILES を追加
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'delete_post.html', {'post': post})

def toiawase(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        emailMessage = EmailMessage(
            to=['fko2347023@stu.o-hara.ac.jp'],
            subject='お問い合わせがありました：{0}'.format(subject),
            body='名前: {0}\nメールアドレス: {1}\n本文: {2}'.format(name, email, message),
        )
        emailMessage.send()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'toiawase.html')
