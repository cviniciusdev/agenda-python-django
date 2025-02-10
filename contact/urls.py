from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('contato/<int:contact_id>/', views.contato, name='contato'),
    path('contato/create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]