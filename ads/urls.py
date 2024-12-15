from .views import register
from .views import AdDetailView, AdListView, DisplayAds, AdCreateView, profile, SuccessView, CustomAuthToken, \
    CSRFTokenView
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from rest_framework.authtoken.views import obtain_auth_token

LoginView.template_name = 'ads/registration/login.html'
LogoutView.template_name = 'ads/registration/logout.html'

urlpatterns = [
    path('', DisplayAds.as_view(), name='ads'),
    # auth and login
    path('register/', register, name='register'),
    path('success/', SuccessView.as_view(), name='success_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api-token-auth/', obtain_auth_token, name='auth_token'),

    # ad CRUD
    path('csrf-token/', CSRFTokenView.as_view(), name='csrf_token'),
    path('', DisplayAds.as_view(), name='home'),
    path('profile/<int:pk>', profile, name='profile'),
    path('ads/', AdListView.as_view(), name='ads'),
    path('ads/new/', AdCreateView.as_view(), name='create_ad'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    # path('ads/<int:pk>/update', AdUpdateView.as_view(), name='update_ad'),
    # path('ads/<int:pk>/delete', AdDeleteView.as_view(), name='delete_ad'),
    # path('ads/search/<slug:search_term>/', search_view, name='search'),
    # path('ads/<int:pk>/comments/new/',
    #      CommentCreateView.as_view(), name='create_comment'),
    # path('comment/<int:pk>/update/',
    #      CommentUpdateView.as_view(), name='update_comment'),
    # path('comment/<int:pk>/delete/',
    #      CommentDeleteView.as_view(), name='delete_comment'),
    # path('comment/<int:pk>/',
    #      CommentDetailView.as_view(), name='view_comment'),
    # path('tags/<slug:tag_slug>/',
    #      AdByTagListView.as_view(), name='tag_ads'),
]
