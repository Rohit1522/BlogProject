from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    
    path('', views.home,name="home"),

    path('home/', views.home,name="home"),
    
    path('welcome/', views.welcome,name="welcome"),

    path('contact/', views.contact,name="contact"),

    path('about/', views.about,name="about"),

    path('SignUp/', views.SignUp,name="SignUp"),

    path('upload/', views.UploadView,name="UploadView"),

    path('ViewBlog/', views.ViewBlog,name="ViewBlog"),

    path('deleteproduct/<pid>', views.DeleteProductView),

    path('detailProduct/<pid>', views.DetailView),

    path('accounts/', include('django.contrib.auth.urls')),

]
#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)