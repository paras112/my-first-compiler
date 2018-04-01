from django.conf.urls import include, url
from django.contrib import admin
from save.views import save
urlpatterns = [
    # Examples:
    # url(r'^$', 'programsave.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^save/$',save,name="save"),

]
