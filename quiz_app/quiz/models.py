from django.db import models

class Exam(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, verbose_name="Descripción")
    created_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

    def get_question_count(self):
        return self.questions.count()

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name="Texto de la pregunta")

    def str(self):
        return self.text[:50]

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200, verbose_name="Texto")
    is_correct = models.BooleanField(default=False, verbose_name="Es correcta")

    def str(self):
        return self.text