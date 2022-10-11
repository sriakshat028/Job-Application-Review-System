from posixpath import basename
from django.urls import path,include
from applications import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.create,name="create"),
    path('description/<int:candidate_id>',views.description,name="description"),

]