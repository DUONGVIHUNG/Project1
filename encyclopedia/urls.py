from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>",views.entry, name="entry"),
    path("wiki/",views.query, name="query"),
    path("createnewpage",views.createpage, name="createnewpage"),
    path("save",views.save, name="save"),
    path("edit",views.edit, name="edit"),
    path("random",views.randomness, name="random")
]
