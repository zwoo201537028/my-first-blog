from django.conf.urls import include, url
from django.contrib import admin
from mysite2.views import HomeView
#from bookmark.views import bookmark_list, bookmark_detail 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^$',HomeView.as_view(),name='home'),
    #url(r'^bookmarks/$', bookmark_list, name='index'),
    #url(r'^bookmarks/(?P<pk>\d+)/$', bookmark_detail, name='detail'), 
]
