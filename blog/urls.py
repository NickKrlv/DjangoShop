from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

app_name = 'blog'
urlpatterns = [
                  path('blogpost_list/', BlogPostListView.as_view(), name='blogpost_list'),
                  path('create/', BlogPostCreateView.as_view(), name='blogpost_create'),
                  path('view/<slug>', BlogPostDetailView.as_view(), name='blogpost_detail'),
                  path('edit/<slug>', BlogPostUpdateView.as_view(), name='blogpost_update'),
                  path('delete/<slug>', BlogPostDeleteView.as_view(), name='blogpost_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
