
from .models import Disease,Forum
from django.shortcuts import render,redirect
from .forms import ForumNew
from django import forms
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'app/index.html',{})

def list(request):
    list=Disease.objects.all()
    return render(request,"app/country_list.html",{'list':list})

def forum(request):
    forum=Forum.objects.all()
    #user=request.user.username
    return render(request,"app/forum_page.html",{'forum':forum})

def detail(request,pk):
	detail=Disease.objects.get(pk=pk)
	return render(request,"app/country_detail.html",{'detail':detail})
@login_required
def forum_new(request):
    
    if request.method=="POST":
    		form=ForumNew(request.POST)
    		if(form.is_valid()):
                        article = form.save(commit=False)
                        article.username = request.user
                        article.save()
                        return redirect("forum")
                    
    else:
        form=ForumNew()
    return render (request,"app/forum_new.html",{'form':form})

    


