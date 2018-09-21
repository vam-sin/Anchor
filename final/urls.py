
from django.contrib import admin
from django.urls import path,include
from news import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('',views.logout,name="logout"),
    path('feed',views.feed,name='feed'),
    path('accounts/',include('accounts.urls')),
    path('news/',include('news.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
