from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page 🚀")

urlpatterns = [
    path("", home),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]