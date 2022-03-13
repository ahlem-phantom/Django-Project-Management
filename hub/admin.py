from django.contrib import admin
from .models import *

class ProjectInline(admin.TabularInline):
    model = Projet
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
        list_filter = [
            'creator',
            'isValid'
        ]
        list_display=(
            'project_name',
            'dure',
            'creator',
            'supervisor',
            'isValid'
        )
        fieldsets = [
            (
                'State',
            {
                'fields': ('isValid',)
            }
            ),
            (
             'About',
             {
                 'fields' : ('project_name',
                 ('creator','supervisor'),
                 'besoin',
                 'description'
                 )
             }   
            ),
            (
             'Duration',
             {
                 'classes' : ('collapse',),
                'fields' :(
                    'dure',
                    'temp_allocated'
                )
             }   
            )
            
        ]
        #radio_fields = {'supervisor': admin.VERTICAL}
        autocomplete_fields = ['supervisor']
        empty_value_display = '-empty-'
      #  readonly_fields =('')

class CoachAdmin(admin.ModelAdmin):
    list_display=(
        'first_name',
        'last_name'
    )
    fields = (
        ('last_name','first_name'),
        'email'
    )
    search_fields = ['last_name','first_name']


class StudentAdmin(admin.ModelAdmin):
    list_display=(
        'first_name',
        'last_name'
    )
    fields = (
        ('last_name','first_name'),
        'email'
    )
    search_fields = ['last_name','first_name']
    inlines =[ProjectInline]
    
   
# ou bien taamel par exp @admin.register(coach) class CoachAdmin(admin.ModelAdmin)
admin.site.register(Coach,CoachAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Projet,ProjectAdmin)
admin.site.register(MemberShip)