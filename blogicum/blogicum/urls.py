from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('blog.urls')),
    path('posts/<int:id>/', include('blog.urls')),
    path('category/<slug:category_slug>/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
