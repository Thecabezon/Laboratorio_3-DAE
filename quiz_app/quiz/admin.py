from django.contrib import admin
from .models import Exam, Question, Choice

# Inline para mostrar las opciones de respuesta dentro de las preguntas
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # Número de opciones adicionales que se mostrarán por defecto

# Inline para mostrar las preguntas dentro de los exámenes
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1  # Número de preguntas adicionales que se mostrarán por defecto

# Configuración del modelo Exam en el admin
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')  # Campos que se mostrarán en la lista de exámenes
    inlines = [QuestionInline]  # Mostrar preguntas relacionadas dentro del examen

# Configuración del modelo Question en el admin
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'exam')  # Campos que se mostrarán en la lista de preguntas
    inlines = [ChoiceInline]  # Mostrar opciones relacionadas dentro de la pregunta

# Configuración del modelo Choice en el admin
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')  # Campos que se mostrarán en la lista de opciones