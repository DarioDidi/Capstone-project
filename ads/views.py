from django.shortcuts import render, redirect

from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
from .forms import ImageForm
from .models import Ad, Image, UserProfile
from .serializers import ImageSerializer
# change to class


def article_create(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.article = request.article  # Associate the image with the article
            image.save()
            return redirect('article_detail', pk=request.article.pk)
    else:
        form = ImageForm()
    return render(request, 'article_form.html', {'form': form})


class DisplayAds(ListView):
    model = Ad

    def get(self, request):
        ads = serialize('json', self.model.objects.all().reverse()[:10])
        return render(request, 'blog/home.html', context={'ads': ads})


class AdDetailView(DetailView):
    model = Ad
    template_name = 'blog/view_ad.html'
    context_object_name = 'ad'

    def get(self, request):
        ad = serialize('json', self.model.objects.get(id=request['pk']))
        images = ImageSerializer(Image.objects.filter(ad=ad))
        return render(request, 'ads/ad_detail.html', context={'ad': ad})
