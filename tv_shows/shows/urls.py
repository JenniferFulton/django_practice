from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_route),
    path('shows', views.all_shows),
    path('shows/new', views.new_show),
    path('create', views.create),
    path('shows/<int:show_id>', views.show_info),
]