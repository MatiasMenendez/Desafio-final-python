from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import Blog
from AppBlog.forms import BlogFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(req):
    return render(req, 'appblog/padre.html')

def about(req):
    return render(req, 'appblog/about.html')


def blogFormulario(req):
    
    if req.method == "POST":
        
        miBlog = BlogFormulario(req.POST)
        print(miBlog)
        
        
        if miBlog.is_valid:
          informacion = miBlog.cleaned_data
          blog = Blog(titulo=informacion["titulo"], subtitulo=informacion["subtitulo"], cuerpo=informacion["cuerpo"], autor=informacion["autor"], fecha=informacion["fecha"], imagen=informacion["imagen"])
          blog.save()
          return render(req,"AppBlog/padre.html")
    else:
        miBlog = BlogFormulario()
     
    return render(req, "AppBlog/blogFormulario.html", {"miBlog": miBlog})

def pages(req):
    
    blogs = Blog.objects.all()
    
    contexto= {"blogs": blogs}
    
    return render(req, "AppBlog/pages.html", contexto)


def eliminarBlog(req, blog_titulo):
    blog = Blog.objects.get(titulo=blog_titulo)
    blog.delete()
    
    blogs = Blog.objects.all()
    
    contexto = {"blogs": blogs}
    
    return render(req, "AppBlog/leerBlogs.html", contexto)


def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                
                return render(request,"AppBlog/padre.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                
                return render(request,"AppBlog/padre.html", {"mensaje":"Error, datos incorrectos"})
        else:
        
         return render(request, "AppBlog/padre.html", {"mensaje": "Error, formulario erroneo"})
     
    form = AuthenticationForm() 
    
    return render(request, "AppBlog/login.html", {'form':form})
    