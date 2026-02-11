from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from . import views
from blogs import views as BlogView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('category/', include('blogs.urls')),
    path('blogs/<slug:slug>/', BlogView.blogs, name='blogs'),

    # search endpoint
    path('search/', BlogView.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),

    # Dashboards
    path('dashboard/', include('dashboards.urls'))
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
