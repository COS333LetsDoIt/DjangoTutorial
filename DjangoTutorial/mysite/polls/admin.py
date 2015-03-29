from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline): #or (admin.StackedInLine)
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date', 'was_published_recently') # displays these fields on the admin page for each question
	fieldsets = [(None, {'fields': ['question_text']}), ('Date information', {'fields': ['pub_date'], 'classes':['collapse']})]
	inlines = [ChoiceInline] # allows the choices belonging to a question to be edited on the question screen
	list_filter = ['pub_date']
	search_fields = ['question_text'] #decides what field the search bar will search for
	list_per_page = 10

admin.site.register(Question, QuestionAdmin) # second argument specifies order in which fields (pub_date and question_text) appears on admin page