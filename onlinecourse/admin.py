from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# <HINT> Register QuestionInline and ChoiceInline classes here
# MY CODE
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# MY CODE
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'is_correct']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)

# <HINT> Register Question and Choice models here
# MY CODE
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

