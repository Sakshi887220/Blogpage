from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

posts = [

	{
		'author': 'James',
		'title': 'Blog Post 1',
		'content' : ' First Post Content',
		'date_posted': 'May 31,2021'
	},

	{
		'author': 'Jaone Doe',
		'title': 'Blog Post 2',
		'content' : ' Second Post Content',
		'date_posted': 'June 2,2021'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request,'blogapp/home.html',context)
	
def about(request):
	return render(request,'blogapp/about.html',{'title':'About Page'})