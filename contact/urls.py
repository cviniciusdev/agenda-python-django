from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('contato/<int:contact_id>/', views.contato, name='contato'),
    path('contato/<int:contact_id>/update/', views.update, name='update'),
    path('contato/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contato/create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    #user
    path('user/create/', views.register, name='register'),    
    path('user/login/', views.login_view, name='login'),    
    path('user/deslogar/', views.logout, name='logout'),    
    path('user/update/', views.user_update, name='user_update'),    
]