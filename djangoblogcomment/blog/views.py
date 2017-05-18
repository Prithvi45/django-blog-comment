
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment


def post_list(request):
	posts = Post.published.all()
	
	return render(request,'blog/post/list.html',{'posts': posts})


def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
	print post.id
	comments = Comment.objects.filter(post_id=post.id)
	print comments
	return render(request,'blog/post/details.html',{'post': post})