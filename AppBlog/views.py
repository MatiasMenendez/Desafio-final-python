from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.models import Blog
from AppBlog.forms import BlogFormulario


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
    
    return render(req, "AppBlog/pages.html", contexto)
