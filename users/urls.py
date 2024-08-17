from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.logreg, name='logreg'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/', views.profile_delete, name='delete'),
]