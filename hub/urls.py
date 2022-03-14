from django.urls import path
from .views import homePage, student_list,coach_list,student_details,StudentListView,studentCreate,studentCreateForm,add_Student,StudentCreateView,StudentUpdateView,StudentDeleteView,LoginPage,register
urlpatterns = [
    path('home/',homePage , name="home"),
    path('listStudent/',student_list,name='listStudent'),
    path('listCoach/',coach_list,name='listCoach'),
    path('st_details/<int:id>',student_details),
    path('listStudents/',StudentListView.as_view(),name='listStudent1'),
    path('StudentCreate/', studentCreate, name='Student_Create'),
    path('StudentCreateForm/', studentCreateForm, name='Student_Create_Form'),
    path('add_Student/', add_Student, name='add_Student'),
    path('StudentCreateView/', StudentCreateView.as_view(), name='StudentCreateView'),
    path('StudentUpdateView/<int:pk>', StudentUpdateView.as_view(), name="StudentUpdateView"),
    path('StudentDeleteView/<int:pk>', StudentDeleteView.as_view(), name="StudentDeleteView"),
    path('LoginPage/', LoginPage.as_view(), name='LoginPage'),
    path('register/', register, name='register'),

]
