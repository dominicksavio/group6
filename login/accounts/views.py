from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .forms import ImageForm
from .forms import ClustersForm
from .models import Image
from .models import Clusters
from .sql import getlonlat,get_img

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
import requests
# from .location import Location
@login_required    
def cluster(req):
    #TODO call dbscan
    # response = requests.get('0.0.0.0:9000')
    
    return render(req,'index.html')
@login_required    
def map(request):
    cluster = Clusters.objects.exclude(cluster=-1)
    return render(request,'map.html',{'cluster':cluster})
@login_required    
def dashboardView(request):
    return render(request,'index.html')
# def home(request,clusterid=-2):
#     if clusterid==-2:
#         if request.method == "POST":
#             form = ImageForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#         form = ImageForm()
#         return render(request, 'myapp/home.html', {'form':form})  
#     else:
#         if request.method == "POST":
#             form1 = ImageForm(request.POST, request.FILES)
#             form2 = ClustersForm(request.POST)
#             print(form1.is_valid())
#             print(form2.is_valid())
#             print(form1)
#             print(form2)
#             if form1.is_valid() and form2.is_valid():
#                 form1.save()
#                 form2.save()

#         obj = get_object_or_404(Clusters, cluster = clusterid)
#         cluster_form = ClustersForm(request.POST or None, instance = obj)
#         # cluster_form = ClustersForm(initial={'cluster':clusterid})
#         image_Form = ImageForm()
#         context = {'cluster_form':cluster_form,'image_Form':image_Form}
#         return render(request, 'myapp/home.html', context)  
@login_required    
def home(request, clusterid=-2):
    if clusterid==-2:
        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        form = ImageForm()
        return render(request, 'myapp/home.html', {'form':form})  
    else:
        
        id=clusterid
        # dictionary for initial data with
        # field names as keys
        context ={}
     
        # fetch the object related to passed id
        obj = get_object_or_404(Clusters, cluster = id)
     
        # pass the object as instance in form
        form = ClustersForm(request.POST or None, instance = obj)
        form1 = ImageForm(request.POST, request.FILES)
        # save the data from the form and
        # redirect to detail_view
        print(form1)
        if form.is_valid() and form1.is_valid():
            fs= form.save(commit=False)
            fs1= form1.save(commit=False)
            print(type(fs1.photo))
            fs.updated_image=fs1.photo
            form.save()
            form1.save()
            return HttpResponseRedirect("/")
            return render(request, "myapp/home.html", context)
     
        # add form dictionary to context
        image_Form = ImageForm()
        context = {'cluster_form':form,'image_Form':form1}
     
        return render(request, "myapp/home.html", context)


@login_required    
def viewImages(request):
    img = Clusters.objects.exclude(updated_image='NA').exclude(cluster=-1)
    latlon=[]
    # for x in img:
        # latlon.append(Location.location(x.photo))
    # return render(request, 'myapp/viewimage.html', {'img':img,'latlon':latlon})  
    return render(request, 'myapp/viewimage.html', {'img':img})  

def registerView(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
       
    else:
        form = SignUpForm()    
    return render(request,'registration/register.html',{'form':form})     
@login_required    
def updateOnCluster(req):
    if req.method == "GET":
        cluster = Clusters.objects.filter(status='NA').exclude(cluster=-1)

        lonlat=[]
        for x in cluster:
            lonlat.append(getlonlat(x.image_hash))

        return render(req,'myapp/clusterSubmit.html', {'cluster':cluster,'lonlat':lonlat})  

