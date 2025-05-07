from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject, Question, Option, MockTestAttempt, UserAnswer
from django.http import HttpResponseNotAllowed
from django.db.models import Sum, Count
import random
# from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'firstapp/index.html')

def start_test(request,subject_id):
    subject=get_object_or_404(Subject, name__iexact=subject_id)
    questions_qs = Question.objects.filter(subject=subject)

    questions=list(questions_qs)
    random.shuffle(questions)  
    questions = questions[:3] 
    #todo: to change number of question to ask
    return render(request, 'firstapp/start_test.html', {'questions': questions, 'subject': subject})



def submit_test(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    subject_id = request.POST.get('subject_id')
    subject = get_object_or_404(Subject, name=subject_id)
    attempt = MockTestAttempt.objects.create(user=request.user, subject=subject, score=0)

    score = 0
    total = 0
    question_ids = request.POST.getlist('question_ids[]')

    for qid in question_ids:
        total += 1
        question = get_object_or_404(Question, id=qid)
        opt_id = request.POST.get(f'question_{qid}')

        if not opt_id:
            UserAnswer.objects.create(
                attempt=attempt, question=question, selected_option=None, is_correct=False
            )
            continue

        option = get_object_or_404(Option, id=opt_id, question=question)
        is_correct = option.is_correct

        UserAnswer.objects.create(
            attempt=attempt,
            question=question,
            selected_option=option,
            is_correct=is_correct
        )

        if is_correct:
            score += 1

    attempt.score = score
    # attempt.save()

    # 🔹 Total score across all attempts
    total_score = MockTestAttempt.objects.filter(user=request.user).aggregate(Sum('score'))['score__sum'] or 0

    # 🔹 Score grouped by subject
    subject_scores = (
        MockTestAttempt.objects
        .filter(user=request.user)
        .values('subject__name')
        .annotate(score_sum=Sum('score'), attempts=Count('id'))
    )

    return render(request, 'firstapp/submit_test.html', {
        'score': score,
        'total': total,
        'subject': subject,
        'total_score': total_score,
        'subject_scores': subject_scores,
    })
