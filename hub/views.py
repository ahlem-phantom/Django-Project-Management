from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Coach
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .forms import StudentForm,StudentModelForm,CustomUserForm
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins  import LoginRequiredMixin
from django.contrib.auth import authenticate,login

# Create your views here.
def homePage(request): 
    return HttpResponse ("<h1> Welcome To The ... </h1>")
    
@login_required
def student_list(request):
    list =Student.objects.all() #activer l orm de django 
    return render(
        request,
        'hub/index.html',
        {
            'students': list,
        }
    )
class StudentListView(LoginRequiredMixin,ListView):
    model= Student
    template_name ="hub/index.html"
   # paginate_by =2 #pour limité l'affichage en 2 etudiants seulement
class StudentDetailView(DetailView):
    model= Student


def student_details(request,id):
    student =Student.objects.get(id=id) #activer l orm de django 
    return render(
        request,
        'hub/st_details.html',
        {
            'student': student,
        }
    )

def coach_list(request):
    listC =Coach.objects.all() #activer l orm de django 
    return render(
        request,
        'hub/index.html',
        {
            'coachs': listC,
        }
    )
def studentCreate(request):
    #print(request)
    if request.method == 'POST':
        firstName=request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        email = request.POST.get('email')

        Student.objects.create(
            first_name=firstName,
            last_name=lastName,
            email=email
        )
        return redirect('listStudent1')
    return render(
        request,
        'hub/add_student.html'
    )



def studentCreateForm(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
        #    Student.objects.create(
        #    first_name = form.cleaned_data.get('first_name'),
        #    last_name = form.cleaned_data.get('last_name'),
        #    email = form.cleaned_data['email']
        #    )
           Student.objects.create(**form.cleaned_data)
           return redirect('listStudent1')

    #print(request)

    return render(
        request,
        'hub/add_student.html',
        {
            'form':form
        }
    )
def add_Student(request):
    form = StudentModelForm()
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save(commit =False)
            #traitement
            student.save()
            return redirect('listStudent1')
    return render(
        request,
        'hub/add_student.html',
        {
            'form' : form
        }
    )

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    template_name = "hub/add_student.html"
    def get_success_url(self):
        return reverse('listStudent1')

class StudentUpdateView(UpdateView):
    #obligatoire juste model+form_class
    model = Student
    form_class = StudentModelForm
    template_name = "hub/add_student.html"
    def get_success_url(self):
        return reverse('listStudent1')
class StudentDeleteView(DeleteView):
    model=Student
    success_url = reverse_lazy('listStudent1')
     #student_confirm_delete.html Pour le redirection 
    #2eme solution
    # def student_delete(request, id) :
    #     student= Student.objects.get(id=id)
    #     student.delete()
    #     return redirect('listStudent1')
class LoginPage(LoginView):
    template_name = "login.html"
    fields ="__all__"
    redirect_autheticated_user =True
    success_url = reverse_lazy('listStudent1')
def register(request):
    form = CustomUserForm()

    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('listStudent1')
            else:
          
                return redirect('login')
    return render(request, "hub/register.html", {'form': form})