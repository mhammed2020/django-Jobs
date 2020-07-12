from django.shortcuts import render
from  .models import  Job
# Create your views here.
def jobList(request):
    jobList = Job.objects.all() # fetch data ==> model queryset
    print(jobList)
    context={
        'jobs':jobList

    }

    return render(request,'job/jobList.html',context)


def jobDetail(request,id):
    jobDetail = Job.objects.get(id=id)  # fetch data ==> model queryset
    print(jobDetail)
    context = {
        'job': jobDetail
    }
    return render(request,'job/jobDetail.html',context)
