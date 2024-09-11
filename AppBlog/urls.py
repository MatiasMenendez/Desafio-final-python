from AppBlog import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView





urlpatterns = [
    path('inicio/', views.inicio, name='padre'),
    path('about/', views.about, name='about'),
    path('blogFormulario/', views.blogFormulario, name='blogFormulario'),
    path('pages/', views.pages, name='pages'),
    path('eliminarBlog/<blog_titulo>/', views.eliminarBlog, name='eliminarBlog'),
    path('logout/', LogoutView.as_view(template_name='AppBlog/padre.html'), name="Logout"),
]