from django.shortcuts import render, redirect

from django.core.serializers import serialize
from django.contrib.auth import login, mixins
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.middleware.csrf import get_token
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import ImageForm, CustomUserForm, UserUpdateForm, CreateAdForm, ProfileUpdateForm
from .models import Ad, Image, UserProfile
from .serializers import ImageSerializer


# # change to class
# def article_create(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.save(commit=False)
#             image.article = request.article  # Associate the image with the article
#             image.save()
#             return redirect('ad_detail', pk=request.article.pk)
#     else:
#         form = ImageForm()
#     return render(request, 'article_form.html', {'form': form})


def register(request):
    # form = {}
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        print("is post req")
        if form.is_valid():
            print("USER REGN FORM VALID")
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('login')
            # return redirect('success_page')
            # return HttpResponseRedirect(reverse('success_page'), status=201)
            # return HttpResponseRedirect(reverse('login'), status=201)
        else:
            print("form:", form)
            print("cleaned_data:", form.cleaned_data)
            print("form errors:", form.error_messages)
    else:
        form = CustomUserForm()
    return render(request, 'ads/register.html', {'form': form})


# class RegisterView(SuccessMessageMixin, CreateView):
#     template_name = 'ads/register.html'
#     success_url = reverse_lazy('login')
#     form_class = CustomUserForm
#     success_message = "Your profile was created successfully"


class SuccessView(DetailView):
    template_name = 'ads/registration_success.html'


# class RegisterView(generics.CreateAPIView):
#     serializer_class = UserSerializer


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'ads/profile.html', context)


class AdCreateView(CreateView, mixins.LoginRequiredMixin, mixins.UserPassesTestMixin):
    model = Ad
    form_class = CreateAdForm
    template_name = 'ads/ad_create.html'
    # success_url = "/"

    def post(self, request, *args, **kwargs):
        print("in ad create view ")
        form = self.get_form()
        if form.is_valid():
            print("in form user id:", request.user.id, "authenticated?", request.user.is_authenticated)
            # owner = User.objects.get(id=request.user.id)
            # form.instance['owner'] = owner
            form.instance.owner = self.request.user
            print("valid form,",form)
            return super().form_valid(form)
        else:
            print("form invalid", form.errors)
            return render(request, 'ads/ad_create.html', {'form': form})

    def get_success_url(self):
        return reverse_lazy('ad_detail', kwargs={'pk': self.object.pk})
    
class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    context_object_name = 'ad'
    # pk_url_kwarg = 'pk'

class AdListView(ListView):
    model = Ad

    def get(self, request):
        print('REQUEST', request)
        ads = {}
        if request.user.is_authenticated:
            ads = serialize('json', self.model.objects.get(
                owner=request.user).reverse()[:10])
        # return render(request, 'home.html', context={'ads': ads})
        return render(request, 'ads/list_ad.html', context={'ads': ads})


class DisplayAds(ListView):
    model = Ad

    def get(self, request):
        # ads = serialize('json', self.model.objects.all().reverse()[:10])
        ads = serialize('json', self.model.objects.all())
        return render(request, 'ads/home.html', context={'ads': ads})


# get an auth token
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

# get a csrf token


class CSRFTokenView(APIView):
    def get(self, request):
        csrf_token = get_token(request)
        return Response({'csrf_token': csrf_token})
