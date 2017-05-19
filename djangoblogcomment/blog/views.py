
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import  CommentForm
from django import template
from django.template.loader import get_template 

def post_list(request):
	posts = Post.published.all()
	
	return render(request,'blog/post/list.html',{'posts': posts})


# def post_detail(request, year, month, day, post):
# 	post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
# 	print post.id
# 	comments = Comment.objects.filter(post_id=post.id)
# 	print comments
# 	return render(request,'blog/post/details.html',{'post': post})


def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
	comments = post.comments.filter(active=True)
	for comment in comments:
		reply = comment.replies.all()
		print reply

	# rpy = Comment.objects.filter(active=True)
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.post = post
			# Save the comment to the database
			new_comment.save()
	else:
		comment_form = CommentForm()

	return render(request,'blog/post/details.html',{'post': post,'comments': comments,'comment_form': comment_form})