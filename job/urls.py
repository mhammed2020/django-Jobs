from django.urls import path
from  . import views
from  . import api
app_name="job"
urlpatterns = [
path('',views.jobList,name = "job_list"),
path('add/',views.addJob,name="add_job"),
path('<str:slug>/',views.jobDetail,name="jobDetail"),


#api 
path('api/list/',api.job_list_api,name="joblistapi"),

]