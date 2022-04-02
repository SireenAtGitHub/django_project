from django.shortcuts import render
from . models import Post

# username = sireengothadiya
# password = testing321


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
