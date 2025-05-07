from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, default=1)
    text = models.TextField()

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
class MockTestAttempt(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE,null=True,default=1)
    score=models.IntegerField(default=0)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.subject.name} - {self.score}"

    
class UserAnswer(models.Model):
    attempt=models.ForeignKey(MockTestAttempt, on_delete=models.CASCADE,related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.attempt.user.username} - {self.question.text[:20]}..."


