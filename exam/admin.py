#_*_coding:utf-8_*_
from django.contrib import admin
from .models import Question,Choice,Content
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class ContentInline(admin.TabularInline):
    model = Content
    extra = 0



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        (None,{'fields':['question_class']}),
        (None,{'fields':['pub_date']}),

        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),

    ]
    inlines = [ChoiceInline,ContentInline]

    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)