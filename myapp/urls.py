from django.conf.urls import include, url
from django.contrib import admin
 
urlpatterns = [
    url('myapp/', include('myapp.urls', namespace='myapp')),
    url('admin/', admin.site.urls),
]