"""yoga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index' ),
    path('about', views.AboutView.as_view(), name='about'),
    path('classes/', views.ClassesView.as_view(), name='classes'),
    path('classes/type/<int:pk>', views.ClassesTypeView.as_view(), name = 'classes-type' ),
    path('classSingle/<int:pk>', views.ClassSingleView.as_view(), name='classSingle'),
    path('single/<int:pk>', views.SingleView.as_view(), name='single'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('content/<int:pk>', views.ContentView.as_view(), name='content'),
    path('yogaBenefits',views.YogaBenefitsView.as_view(), name='yogaBenefits'),
    path('moreYoga',views.MoreYogaView.as_view(), name='moreYoga'),
    path('contact', views.contactview, name='contact'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('comment/<int:pk>',views.commentview ,name='comment'),
    path('search/', views.search, name='search')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

