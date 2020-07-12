from django.shortcuts import render, redirect
from django.urls import reverse

from  .models import  Job

from django.core.paginator import Paginator

from  . froms import ApplyForm,JobForm
# Create your views here.
def jobList(request):
    jobList = Job.objects.all() # fetch data ==> model queryset

    paginator = Paginator(jobList, 3)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # print(jobList)
    context={
        'jobs':page_obj

    }

    return render(request,'job/jobList.html',context)


def jobDetail(request , slug):
    jobDetail = Job.objects.get(slug=slug)  # fetch data ==> model queryset
    # print(jobDetail)
    if request.method=='POST':
        form = ApplyForm(request.POST,request.FILES)
        print("inside post")
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = jobDetail
            myform = form.save()
    else :
        form = ApplyForm()
    context = {
        'job': jobDetail,
        'form1': form
    }
    return render(request,'job/jobDetail.html',context)


def addJob(request):

    if request.method=='POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else :
        form = JobForm()
    context = {
        'form2':form,
    }
    return  render(request,'job/add_job.html',context)
