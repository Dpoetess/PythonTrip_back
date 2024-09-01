from django.contrib import admin
from django.urls import include, path

BASE_URL = 'api/v1/'
urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_URL, include('users.urls')),
    path(BASE_URL, include('itineraries.urls')),
    path(BASE_URL, include('countries.urls')),
    path(BASE_URL, include('preferences.urls')),
    path(BASE_URL, include('mycollections.urls'))

]
