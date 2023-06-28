from django.urls import path
from . import views 

app_name="App_Home"

urlpatterns = [
    path('',views.index,name='index'),
    path('notice/<pk>/',views.notice,name='notice'),
    path('all_notice/',views.notice_page,name='allnotice'),
    path('gallery/',views.gallery,name='gallery'),
    path('donation/',views.donation,name='donation'),
    path('admission/',views.Admission,name='admission'),
    path('academic/',views.Academic,name='academic'),
    path('contact/',views.contact,name='contact'),
    path('create_notice/',views.NoticeCreateView.as_view(),name='create_notice'),
    path('create_gallery/',views.GalleryCreateView.as_view(),name='create_gallery'),
    path('update_notice/',views.NoticeListView.as_view(),name='update_notice'),
    path('notice_edit/<pk>',views.EditNotice.as_view(),name='notice_edit'),
    path('notice_delete/<pk>',views.NoticeDelete,name='notice_delete'),

    path('update_gallery/',views.GalleryListView.as_view(),name='update_gallery'),
    path('gallery_edit/<pk>',views.EditGallery.as_view(),name='gallery_edit'),
    path('gallery_delete/<pk>',views.GalleryDelete,name='gallery_delete'),
]