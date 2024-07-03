from django.shortcuts import render
from django.http import HttpResponse
from .models import CONTACT, SKILL, EXPERIENCE, PROJECT, EDUCATION

# Create your views here.
intro = {'Name': 'Alisha Masood', 'Occ1': 'Web Developer', 'Occ2': 'Software Engineer', 'Tagline': 'Working with determination and consistancy'}
ob1 = SKILL.objects.all()
skill = {'skill1': ob1}
ob2 = EXPERIENCE.objects.all()
exp = {'exper': ob2}
ob3 = PROJECT.objects.all()
proj = {'p': ob3}
ob4 = EDUCATION.objects.all()
educa = {'e': ob4}

def index(request):

    return render(request, 'mainPage.html', {'intro': intro, 'skill': skill, 'experience': exp, 'pro': proj, 'edu': educa})


def message(request):
    if request.method == 'POST':
        n = request.POST['name']
        em = request.POST['email']
        msg = request.POST['message']
        obj = CONTACT()
        obj.name = n
        obj.email = em
        obj.message = msg
        try:
            obj.save()
            return render(request, 'mainPage.html', {'intro': intro, 'skill': skill, 'experience': exp, 'pro': proj, 'edu': educa})
        except:
            return HttpResponse("Message failed, please go back to the previous screen and try again")
    else:
        return HttpResponse("Error")
