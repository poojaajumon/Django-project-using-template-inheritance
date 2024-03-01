from django.shortcuts import render,redirect
from .models import Article
from django.utils import timezone
from django.contrib import messages

def index(request):
    data={
        "art":Article.objects.all()
        
    }
    return render(request,'index.html',data)

def about(request):
    return render(request,'about.html')

def posts(request):
    return render(request,'more_posts.html')

def add(request):
    if request.method=="POST":
        head=request.POST.get('head')
        para=request.POST.get('para')
        image=request.FILES.get('image')
        date = timezone.now()
        query=Article(head=head,para=para,image=image,date=date)
        query.save()
        messages.success(request,"Details Added Successfully")
        # return redirect("/")
    return render(request,'admin.html')

def detailed(request,id):
    data={
        "blog":Article.objects.get(id=id)
        
    }
    return render(request,'details.html',data)

def delete(request,id):
    dlt=Article.objects.get(id=id)
    dlt.delete()
    return redirect("/")


    
def edit(request, id):
    if request.method == "POST":
        head = request.POST.get('head')
        para = request.POST.get('para')
        image = request.FILES.get('image')

        edit_article = Article.objects.get(id=id)

        edit_article.head = head
        edit_article.para = para

        if image:
            edit_article.image = image

        edit_article.save()

        messages.success(request, "Details Updated Successfully")
        return render(request, 'edit.html', {'blog': edit_article})
    else:
        data = {
            "blog": Article.objects.get(id=id)
        }
        return render(request, 'edit.html', data)