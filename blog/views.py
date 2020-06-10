from django.shortcuts import render
from blog.forms import SignupForm,UploadForm
from blog.models import Contact,Upload
from  django.contrib.auth.decorators import login_required 
# Create your views here.
def home(request):
    return render(request,'blog/index.html')


def welcome(request):
    return render(request,'blog/welcome.html')
    
@login_required
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
    return render(request,'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')

def SignUp(request):
    signupform=SignupForm()
    mydict ={'signupform':signupform}
    if request.method=='POST':
        signupform=SignupForm(request.POST);
        user=signupform.save();
        user.set_password(user.password)
        user.save();
        mydict.update({'mag':'Registered Successfully'})
    return render(request,'blog/signup.html',context=mydict)

@login_required
def UploadView(request):
    uploadform=UploadForm()
    mydict={'uploadform':uploadform}
    if request.method=='POST':
        uploadform=UploadForm(request.POST,request.FILES);
        if uploadform.is_valid():
            data=uploadform.save(commit=False)
            data.author=request.user
            data.save()
            mydict.update({'msg':'Data Saved Successfully'})
    return render(request,'blog/upload.html',context=mydict)

@login_required
def ViewBlog(request):
    images=Upload.objects.all().order_by('-upload_date')
    return render(request,'blog/viewblog.html',{'images':images})


@login_required
def DetailView(request,pid):
    #select * from product where id='1'
    images=Upload.objects.get(id=pid)
    #images.delete();  delete records
    return render(request,'blog/detailview.html',{'images':images})    

def DeleteProductView(request,pid):
    images=Upload.objects.get(id=pid)
    images.delete(); #delete records
    images=Upload.objects.all().order_by('-upload_date')
    return render(request,'blog/viewblog.html',{'images':images,'msg':'Product Deleted'})