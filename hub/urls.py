from django.urls import path
from .views import homePage, student_list,coach_list,student_details
urlpatterns = [
    path('home/',homePage , name="home"),
    path('listStudent/',student_list),
    path('listCoach/',coach_list),
    path('st_details/<int:id>',student_details),

]
