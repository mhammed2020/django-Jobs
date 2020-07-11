from django.urls import path
from  . import views
urlpatterns = [
path('',views.jobList),
path('<int:id>/',views.jobDetail),
]