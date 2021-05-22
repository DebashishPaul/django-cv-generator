from django.shortcuts import render
from .models import Profile
# Create your views here.
def FormView(request):
    if request.method=="POST":
        name = request.POST.get("name","")
        title = request.POST.get("title","")
        email = request.POST.get("email","")
        about = request.POST.get("about","")
        previous_work = request.POST.get("previous_work","")
        phone = request.POST.get("phone","")
        university = request.POST.get("university","")
        facebook_url = request.POST.get("facebook_url","")

        profile = Profile(name=name, title=title, email=email, about=about, previous_work=previous_work, phone=phone, university=university, facebook_url=facebook_url)
        profile.save()
    return render(request, 'pdf/accept.html')

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    return render(request, 'pdf/resume.html', {'user_profile':user_profile})