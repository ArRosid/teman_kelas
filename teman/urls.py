from django.urls import path

from teman.views import *

urlpatterns = [
    path("", TemanListView.as_view()),
    path("add/", TemanCreateView.as_view(), name="tambah_teman"),
    path("delete/<pk>/", TemanDeleteView.as_view(), name="delete_teman"),
]