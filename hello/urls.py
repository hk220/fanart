from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("hello/", TemplateView.as_view(template_name="hello/hello.html")),
]
