from django import forms
from .models import Exam, Question, Choice

# Formulario para crear/editar exámenes
class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter exam title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter exam description'
            }),
        }
        labels = {
            'title': 'Exam Title',
            'description': 'Exam Description'
        }

# Formulario para crear/editar preguntas
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Enter your question here'
            }),
        }
        labels = {
            'text': 'Question Text'
        }

# Formulario para crear/editar opciones de respuesta
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text', 'is_correct']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter answer choice'
            }),
            'is_correct': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'text': 'Choice Text',
            'is_correct': 'Correct Answer'
        }

# Crear un FormSet para manejar múltiples opciones de respuesta
# Este FormSet permitirá crear/editar múltiples opciones para una pregunta
ChoiceFormSet = forms.inlineformset_factory(
    Question,  # Modelo padre
    Choice,    # Modelo hijo
    form=ChoiceForm,
    extra=4,   # Número de formularios vacíos a mostrar
    min_num=2, # Mínimo número de opciones requeridas
    max_num=4, # Máximo número de opciones permitidas
    validate_min=True,
    validate_max=True,
    can_delete=False
)