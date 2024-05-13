from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("DownloadAndGenerateData", views.retrieve_json_and_get_data, name=""),
]

