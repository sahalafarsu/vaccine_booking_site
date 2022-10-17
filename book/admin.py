


from django.contrib import admin
# from django.contrib.admin import ModelAdmin

from .models import District, Center, People


# Register your models here.
class districtAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(District,districtAdmin)

class centerAdmin(admin.ModelAdmin):
    list_display = ['name','stock','available','updated']
    list_editable = ['stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Center,centerAdmin)

class peopleAdmin(admin.ModelAdmin):
    list_display = ['first_name','birthday','gender','email','phone','house_name','city','district','pincode']
    list_per_page = 20
admin.site.register(People,peopleAdmin)