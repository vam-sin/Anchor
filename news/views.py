from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import News
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CommentForm


def home(request):
    return render(request,'news/home.html')

@login_required
def account(request):
    return render(request,'news/account.html')

@login_required
def feed(request):
    news=News.objects
    return render(request,'news/feed.html',{'news':news})

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('feed')
        else:
            return render(request,'news/home.html',{'error':'Username or password is incorrect.'})
    else:
        return render(request,'news/home.html')

@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image']:
            news=News()
            news.title=request.POST['title']
            news.body=request.POST['body']
            news.icon=request.FILES['icon']
            news.image=request.FILES['image']
            news.pub_date=timezone.datetime.now()
            news.sailor=request.user
            news.save()
            return redirect('/news/' + str(news.id))


        else:
            return render(request,'news/create.html',{'error':'All fields are required.'})

    else:
        return render(request,'news/create.html')

@login_required
def detail(request,news_id):
    news=get_object_or_404(News,pk=news_id)
    return render(request,'news/detail.html',{'news':news})

@login_required
def love(request,news_id):
    if request.method=='POST':
        news=get_object_or_404(News,pk=news_id)
        news.votes_total+=1
        news.save()
        return redirect('/news/' + str(news.id))

@login_required
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')

@login_required
def add_comment_to_post(request,news_id):
    news=get_object_or_404(News,pk=news_id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = news
            comment.save()
            return redirect('/news/'+str(news.id))
    else:
        form = CommentForm()

    return render(request, 'news/add_comment_to_post.html', {"form": form})

# @login_required
# def userprofile(request,news_id):
#     user = request.user
#     news=get_object_or_404(News,pk=news_id)
#     user_posts = news.objects.filter(sailor=request.user).order_by('-pub_date')
#     template = 'news/account.html'
#     return render(request, template, {'user_posts':user_posts,'user': user})
