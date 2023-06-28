from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from App_Login.models import Teacher 
from .forms import UpdateProfileForm
# Create your views here.

def LoginView(request):
    if request.user.is_authenticated:
        return redirect(reverse('App_Login:profile'))
    else:
        form=AuthenticationForm()
        if request.method=="POST":
            form=AuthenticationForm(data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect(reverse('App_Login:profile' ))
        dict={'form':form,
        'title':"User login form"
        }
        return render(request, 'App_Login/login.html', context=dict)
@login_required
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Home:index' ))
@login_required
def Profile(request):
    dict={
        'title':"Profile"
    }
    return render(request, 'App_Login/profile.html', context=dict)

@login_required
def UpdateProfile(request):
    current_user=request.user
    # print(current_user.username)
    check_user=Teacher.objects.filter(teacher=current_user)
    # print(check_user)
    if(check_user):
        current_user=Teacher.objects.get(teacher=current_user)
        # print(current_user)
        form=UpdateProfileForm(instance=current_user)
        if request.method=='POST':
            form=UpdateProfileForm(request.POST, request.FILES,instance=current_user)
            if form.is_valid():
                form.save()
                return redirect(reverse('App_Login:profile'))
    else:
        form = UpdateProfileForm()
        if request.method=='POST':
            form=UpdateProfileForm(request.POST, request.FILES, request.FILES)
            if form.is_valid():
                form_obj=form.save(commit=False)
                form_obj.teacher=current_user 
                form_obj.save()
                return redirect(reverse('App_Login:profile'))
    
    dict={
        'title':"Update Profile",
        'form':form
    }
    return render(request, 'App_Login/update_profile.html', context=dict)

def TeacherList(request):
    teacher=Teacher.objects.all()
    dict={
        'teachers':teacher
    }
    return render(request, "App_Login/teacher_list.html", context=dict)

def TeacherDetails(request,pk):
    teacher=Teacher.objects.get(pk=pk)
    dict={
        'teacher':teacher
    }
    return render(request, "App_Login/teacher_details.html", context=dict)
    
    
    
