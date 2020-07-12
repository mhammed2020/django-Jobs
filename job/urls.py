from django.urls import path
from  . import views
app_name="job"
urlpatterns = [
path('',views.jobList,name = "job_list"),
path('add/',views.addJob,name="add_job"),
path('<str:slug>/',views.jobDetail,name="jobDetail"),
]