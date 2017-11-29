"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from my_bookstore import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^book/(?P<title>.+)/(?P<book_id>[0-9]+)', views.book_page, name='book'),
    url(r'^category/(?P<cat>.+)', views.cat_page, name='book'),
    url(r'^author/(?P<author>.+)/(?P<author_id>[0-9]+)', views.author_page, name='author'),
    url(r'^admin/', admin.site.urls),
    url(r'^test_forms/', views.test_forms),
]

# user account related
urlpatterns += [
url(r'^signup/$', views.signup, name='signup'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
