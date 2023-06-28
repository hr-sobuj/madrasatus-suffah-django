from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Blog.models import Blog,BlogCatagory
import uuid
from django.urls import reverse,reverse_lazy
from django.core.paginator import Paginator
from .forms import CreateBlogPostForm
# Create your views here.


# @login_required 
# def CreateBlogPost(request):
#     form=CreateBlogPostForm()
#     if request.method=="POST":
#         form=CreateBlogPostForm(request.POST)

#     dict={
#         'form':form
#     }
#     return render(request, "App_Blog/create_blog.html", context=dict)
    


class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "App_Blog/create_blog.html"
    fields=('blog_title','catagory','blog_content','blog_image')

    def form_valid(self,form):
        form_obj=form.save(commit=False)
        form_obj.author=self.request.user
        title=form_obj.blog_title
        form_obj.slug=title.replace(" ","-")+"-"+str(uuid.uuid4())
        form_obj.save()
        return HttpResponseRedirect(reverse_lazy('App_Login:profile'))

def BlogDetailsView(request,pk):
    blog=Blog.objects.get(pk=pk)
    recent=Blog.objects.all()
    catagory=BlogCatagory.objects.all()
    dict={"blog":blog,
    "recent":recent,
    "catagory":catagory
    }
    return render(request, "App_Blog/blog_details.html", context=dict)

class EditBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "App_Blog/edit_blog.html"
    fields = ('blog_title', 'blog_content', 'blog_image')
    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Login:profile')
class BlogListView(LoginRequiredMixin,ListView):
    context_object_name="blog_list"
    model=Blog 
    template_name="App_Blog/blog_list.html"
    fields=('blog_title','blog_image')

@login_required 
def BlogDelete(request,pk):
    post=Blog.objects.get(pk=pk).delete()
    return redirect(reverse('App_Blog:list'))

def BlogPage(request):
    recent=Blog.objects.all()
    catagory=BlogCatagory.objects.all()
    paginator=Paginator(recent,15)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    dict={"recent":page_obj,"catagory":catagory}
    return render(request, "App_Blog/blog.html", context=dict)

def BlogCat(request,pk):
    cat=BlogCatagory.objects.get(pk=pk)
    blog=Blog.objects.filter(catagory=cat)
    paginator=Paginator(blog,15)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    dict={
        'recent':page_obj,
        'cat':cat,

    }
    return render(request, "App_Blog/catagory.html", context=dict)
    
    




    