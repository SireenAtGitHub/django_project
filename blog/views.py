from django.shortcuts import render
# username = sireengothadiya
# password = testing321
posts = [
	{
		'author' : 'Sireen',
		'title' : 'Blog First Post',
		'content' : 'Content goes here.. blah blah blah',
		'date_posted' : 'July 20, 2000'
	},
	{
		'author' : 'Maitri',
		'title' : 'Blog Second Post',
		'content' : 'New second content blah blah blah',
		'date_posted' : 'January 23, 2000'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html',{'title' : 'About'})
# Create your views here