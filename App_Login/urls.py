from django.urls import path
from App_Login import views 

app_name="App_Login"

urlpatterns = [
    path('login/',views.LoginView,name='login'),
    path('logout/',views.LogoutView,name='logout'),
    path('profile/',views.Profile,name='profile'),
    path('update_profile/',views.UpdateProfile,name='update_profile'),
     path('teacher_list/',views.TeacherList,name='teacher_list'),
     path('teacher_details/<pk>/',views.TeacherDetails,name='teacher_details'),
]