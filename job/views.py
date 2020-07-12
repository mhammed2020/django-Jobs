from django.shortcuts import render
from  .models import  Job

from django.core.paginator import Paginator
# Create your views here.
def jobList(request):
    jobList = Job.objects.all() # fetch data ==> model queryset

    paginator = Paginator(jobList, 1)  # Show 25 contacts per page.
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
    context = {
        'job': jobDetail
    }
    return render(request,'job/jobDetail.html',context)
