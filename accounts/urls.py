from django.urls import path
from  . import views
app_name="job"
urlpatterns = [
path('signup/',views.signUp,name = "sign_up"),
path('profile/',views.profile,name = "profile"),
path('profile/edit/',views.profileEdit,name = "profile_edit"),

]