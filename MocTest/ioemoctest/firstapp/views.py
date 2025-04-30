from django.shortcuts import render
from .models import Question, Option, UserAnswer, UserScore
# from django.contrib.auth.decorators import login_required
import random
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'firstapp/index.html')

# @login_required
def question_page(request):
    # Load all questions
    questions = list(Question.objects.all())
    if not questions:
        return render(request, 'firstapp/question_page.html', {'error': 'No questions available.'})

    random.shuffle(questions)
    question = questions[0]  # Just pick the first one after shuffling

    options = question.options.all()

    if request.method == 'POST':
        selected_option_id = request.POST.get("selected_option")

        if selected_option_id:
            selected_option = Option.objects.get(id=selected_option_id)
            UserAnswer.objects.create(
                user=request.user,
                question=question,
                selected_option=selected_option
            )
            score = 1 if selected_option.is_correct else 0
        else:
            score = 0

        UserScore.objects.create(user=request.user, score=score, date_taken=timezone.now())
        # return render(request, 'firstapp/score.html', {'score': score})

    return render(request, 'firstapp/question_page.html', {
        'question': question,
        'options': options
    })