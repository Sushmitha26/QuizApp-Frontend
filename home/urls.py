from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('quiz/', views.quiz, name='quiz'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('adminpage/create/', views.create_quiz, name='create_quiz'),
    path('adminpage/update/', views.update_quiz, name='update_quiz'),
    path('adminpage/delete/', views.delete_quiz, name='delete_quiz'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout')
]