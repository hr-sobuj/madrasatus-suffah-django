from django.urls import path
from App_Blog import views 

app_name="App_Blog"

urlpatterns = [
    path('create/',views.CreateBlogView.as_view(),name='create'),
    # path('create/',views.CreateBlogPost,name='create'),
    path('details/<pk>',views.BlogDetailsView,name='details'),
    path('edit/<pk>',views.EditBlog.as_view(),name='edit'),
    path('delete/<pk>',views.BlogDelete,name='delete'),
    path('blog_page/',views.BlogPage,name='blog'),
    path('catagory/<pk>',views.BlogCat,name='catagory'),
    path('list/',views.BlogListView.as_view(),name='list'),
]