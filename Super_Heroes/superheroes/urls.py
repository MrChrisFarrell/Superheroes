from . import views
from django.urls import path

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('<int:superhero_id>/', views.detail, name='detail')
]