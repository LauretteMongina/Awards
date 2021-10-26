from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, PostForm, UpdateUserForm, UpdateUserProfileForm, RatingForm
from rest_framework import viewsets
from .models import Profile, Post, Rating
from .serializer import ProfileSerializer, UserSerializer, PostSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
import random
import cloudinary
import cloudinary.uploader
import cloudinary.api
import datetime as dt
import statistics


# Create your views here.
class UserList(viewsets.ModelViewSet):
    def get(self,request,format=None):
        all_users=User.objects.all()
        user_serializers = UserSerializer(all_users,many=True)
        return Response(user_serializers.data)

class ProjectList(APIView):
    def get(self,request,format=None):
        all_projects = Project.objects.all()
        project_serializers = ProjectSerializer(all_projects, many=True)
        return Response(project_serializers.data)  

class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        profile_serializers = ProfileSerializer(all_profiles, many=True)
        return Response(profile_serializers.data)  


def index(request):
    posts = Post.objects.all()
    date = dt.date.today()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    return render(request, 'index.html', {'posts': posts, 'form': form,'date':date})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            email = form.cleaned_data.get('email')
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})



@login_required(login_url='login')
def project(request, post):
    post = Post.objects.get(title=post)
    ratings = Rating.objects.filter(user=request.user, post=post).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_rating = Rating.objects.filter(post=post)
            
            usability_rating = [usability.usability for us in post_rating]
            usability_average = statistics.mean(usability_rating)
            
            design_rating = [design.design for design in post_rating]
            design_average = statistics.mean(design_rating)

            content_ratings = [content.content for content in post_rating]
            content_average = statistics.mean(content_rating)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingForm()
    params = {
        'post': post,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request, 'project.html', params)

# def search_results(request):
#     if 'post' in request.GET and request.GET['post']:
#         title = request.GET.get("post")
#         search = Post.search_by_title(title)
#         message = f'{title}'

#         return render(request, 'search.html',{'message':message, 'search':search})
@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(developer=request.user).order_by('-created_at')
    # user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile':profile,
        'posts':posts,
    }
    return render(request, 'profile.html', params)