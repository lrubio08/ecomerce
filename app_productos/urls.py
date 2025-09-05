from django.urls import path
from . import views 

urlpatterns = [
    path("smartphone/", views.smartphone, name="smartphone"),
    path("notebook/", views.notebook, name="notebook"),
    path("tablet/", views.tablet, name="tablet"),   
    path("pc_escritorio/", views.pc_escritorio, name="pc_escritorio"),
    path("televisor/", views.televisor, name="televisor"),
]