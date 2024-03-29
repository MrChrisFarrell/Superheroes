from . import views
from django.urls import path

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:superhero_id>/', views.edit, name='edit'),
    path('delete/<int:superhero_id>/', views.delete, name='delete'),
    path('<int:superhero_id>/', views.detail, name='detail')
]