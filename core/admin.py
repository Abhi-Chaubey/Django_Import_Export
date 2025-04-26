from django.contrib import admin
from core.models import Input, Reference, Output

@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    list_display = ['field1', 'field2', 'field3', 'field4', 'field5', 'refkey1', 'refkey2']

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['refkey1', 'refdata1', 'refkey2', 'refdata2', 'refdata3', 'refdata4']

@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = ('outfield1', 'outfield2', 'outfield3', 'outfield4', 'outfield5', 'created_at')
