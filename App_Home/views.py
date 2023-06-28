from django.shortcuts import render,HttpResponseRedirect,redirect
from App_Blog.models import Blog 
from App_Home.models import Notice,Gallery
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
# Create your views here.
def index(request):
    blog=Blog.objects.all()
    notice=Notice.objects.all()
    marqueetext=Notice.objects.all()
    dict={
        'blog':blog,
        'notices':notice,
        'title':"Madrasatus Suffah",
        'marqueetext':marqueetext
    }
    return render(request, 'App_Home/index.html', context=dict)

def notice(request,pk):
    notice=Notice.objects.get(pk=pk)
    dict={
        'notice':notice
    }
    return render(request, 'App_Home/notice_detail.html', context=dict)
def notice_page(request):
    notice=Notice.objects.all()
    paginator=Paginator(notice,15)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    dict={"notices":page_obj}
    return render(request, 'App_Home/notice.html', context=dict)


def gallery(request):
    gallery=Gallery.objects.all()
    paginator=Paginator(gallery,100)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    dict={
        'gallery':page_obj,
    }
    return render(request, "App_Home/gallery.html", context=dict)

def donation(request):
    return render(request, "App_Home/donation.html", {})

def contact(request):
    return render(request, "App_Home/contact.html", {})


class NoticeCreateView(LoginRequiredMixin,CreateView):
    model = Notice
    template_name = "App_Home/create_notice.html"
    fields=('notice_title','notice_pdf')
    def form_valid(self,form):
        form=form.save()
        return HttpResponseRedirect(reverse_lazy('App_Login:profile'))

class NoticeListView(LoginRequiredMixin,ListView):
    context_object_name="notice_list"
    model=Notice 
    template_name="App_Home/update_notice.html"
    fields=('notice_title','notice_pdf')


class EditNotice(LoginRequiredMixin, UpdateView):
    model = Notice
    template_name = "App_Home/edit_notice.html"
    fields = ('notice_title', 'notice_pdf')
    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Login:profile')

@login_required 
def NoticeDelete(request,pk):
    post=Notice.objects.get(pk=pk).delete()
    return redirect(reverse('App_Home:update_notice'))


class GalleryCreateView(LoginRequiredMixin,CreateView):
    model = Gallery
    template_name = "App_Home/create_gallery.html"
    fields=('caption','image')
    def form_valid(self,form):
        form=form.save()
        return HttpResponseRedirect(reverse_lazy('App_Login:profile'))

class GalleryListView(LoginRequiredMixin,ListView):
    context_object_name="gallery_list"
    model=Gallery 
    template_name="App_Home/update_gallery.html"
    fields=('caption','image')


class EditGallery(LoginRequiredMixin, UpdateView):
    model = Gallery
    template_name = "App_Home/edit_gallery.html"
    fields = ('caption', 'image')
    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Login:profile')

@login_required 
def GalleryDelete(request,pk):
    post=Gallery.objects.get(pk=pk).delete()
    return redirect(reverse('App_Home:update_gallery'))

    
def Academic(request):
    return render(request, "App_Home/academic.html", {})

def Admission(request):
    return render(request, "App_Home/adminssion.html", {})