from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Image,Profile,Comments,Followers

# Create your views here.
def index(request):
    title='Home'
    return render(request,"index.html",{"title":title})


def profile(request):
    try:
        current_user=request.user.id
        profile_photos=Image.objects.filter(userId=current_user)
        profile_image=Profile.objects.filter(userId=current_user).all()
        profile=profile_image.reverse()[0:1]

    except Exception as e:
        raise Http404()

    return render(request,"profile.html",{'profile':profile_photos,"pic":profile})


def uploads(request):
    title='Upload'
    current_user=request.user
    current_user_id=request.user.id
    if request.method=='POST':
        form=PostImage(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.user=current_user
            image.userId=current_user_id
            image.profile=current_user_id
            image.save()
        return redirect("profile")
    else:
        form=PostImage()
    return render(request,"upload.html",{"title":title,"form":form})    
