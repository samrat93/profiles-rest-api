from django.urls import path

form profiles_api import views


urlpatterns = [
    path('hello-view/',view.HelloApiView.as_view())
]
