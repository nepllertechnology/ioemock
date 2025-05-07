from django.contrib import admin
from .models import Question, Option, UserAnswer, Subject, MockTestAttempt

# Register your models here.




class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # show 4 empty option fields

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('text', 'subject')
    list_filter = ('subject',)
    search_fields = ('text',)

admin.site.register(Subject)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserAnswer)
admin.site.register(MockTestAttempt)
