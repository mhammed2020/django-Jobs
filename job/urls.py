from django.urls import path
from  . import views
app_name="job"
urlpatterns = [
path('',views.jobList),
path('<int:id>/',views.jobDetail,name="jobDetail"),
]