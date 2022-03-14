from django.contrib import admin, messages
from .models import *
# Register your models here.
#class ProjectInLine(admin.TabularInline):  //pour afficher les champs horizantalement
#class ProjectInLine(admin.StackedInline):  //pour afficher les champs verticalement
class ProjectInLine(admin.StackedInline):
    model=Projet

class StudentAdmin(admin.ModelAdmin):
    list_display =(
         'first_name',
        'last_name'
    )
    #Organisation
    fields =(
        ( 'first_name','last_name'),
        'email'
    )
    #Recherche
    search_fields =['last_name','first_name']
    inlines = [ProjectInLine]
#@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display =(
         'first_name',
        'last_name'
    )
    #Organisation
    fields =(
        ( 'first_name','last_name'),
        'email'
    )
    #Recherche
    search_fields =['last_name','first_name']

#filtrer par rapport au durée
class ProjectDurationFilter(admin.SimpleListFilter):
    parameter_name="dure"
    title = "Durée"

    def lookups(self,request, model_admin):
        return (
            ('1 Month','less than 1 month'),
            ('3 Months','less than 3 month'),
            ('4 Months','More than 3 month'),
           
        )
    def queryset(self,request, queryset):
        if self.value() == "1 Month":
            return queryset.filter(dure__lte=30)
        if self.value() == "3 Months":
            return queryset.filter(dure__gt=30,dure__lte=90)
        if self.value() == "4 Months":
            return queryset.filter(dure__gt=90)
#Modifier les projets non valide en des projets valide
def set_Valid (model_admin, request, queryset):
    rows = queryset.update(isValid=True)
    if rows == 1:
        msg = "1 project was"
    else:
        msg = f"{rows} projects were"
    messages.success(request,message =f"{msg} successfully marked as valid")

set_Valid.short_description = "Validate"
#Modifier les projets valide en des projets non valide
def set_inValid (model_admin, request, queryset):
    number = queryset.filter(isValid=False)
    if number.count()> 0:
        messages.error(request, "Projects already set to Not Valid")
    else :
        rows = queryset.update(isValid=False)
        if rows == 1:
            msg = "1 project was"
        else:
            msg = f"{rows} projects were"
        messages.error(request,message =f"{msg} successfully marked as inValid")

set_inValid.short_description = "inValidate"
class ProjetAdmin(admin.ModelAdmin):
    actions =[set_Valid,set_inValid]
    actions_on_bottom = True
    actions_on_top = True
    list_filter = (
        'creator',
        'isValid',
        ProjectDurationFilter
    )
    list_display =(
         'project_name',
        'dure',
        'supervisor',
        'isValid'
    )
    fieldsets= [
        (
            'State', #'State' : pour ajouter un titre / None : pour n'ajouter pas un titre
            {
                'fields':('isValid',)
            }
        ),
        (
            'About',
            {
                'fields':(
                    'project_name',
                     ('creator','supervisor'),
                     'besoin',
                    'description'  
                )   
            }
        ),
        (
            'Durations',
            {
                'classes': ('collapse',), #pour le choix d'afficher ou de cacher 
                'fields':(
                    'dure',
                    'temp_allocated'
                )
            }
        )

    ]
    #radio_fields = {'supervisor': admin.VERTICAL} #pour afficher la liste des superviseur sous forme de radioButton
    autocomplete_fields= ['supervisor']  #admet un recherche de superviseur selon la liste trouver
    empty_value_display = '-empty-' #dans les champs vide il affiche "empty"


admin.site.register(Student,StudentAdmin)
admin.site.register(Coach,CoachAdmin)
admin.site.register(Projet,ProjetAdmin)
admin.site.register(MemberShip)

