from django.contrib import admin
from .models import Question, Option, UserAnswer, UserScore

# Register your models here.

admin.site.register(UserAnswer)
admin.site.register(UserScore)

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # show 4 empty option fields

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Question, QuestionAdmin)
