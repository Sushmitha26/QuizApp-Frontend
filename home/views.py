from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Choice, Admin
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
 
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def quiz(request):
    try:
        if request.method == 'GET':
            questions_list = Question.objects.all()
            context = {
                'questions_list': questions_list
            }

        if request.method == 'POST':
            print('submitted ans:', request.POST.items())
            correct_answers = 0

            for key, val in request.POST.items():
                print('kv:',key, val)
                if key.startswith('choice'):
                    selected_choice = Choice.objects.get(id=val)
                    if selected_choice.is_correct == True:
                        correct_answers += 1

            return render(request, 'home/results.html', {'correct_answers': correct_answers})


    except:
        messages.info(request,'Something went wrong!!')
        return redirect('/home')

    return render(request, 'home/quiz.html', context)


def adminpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user = Admin.objects.get(username = username)
            if password == user.password:
                questions = Question.objects.all()
                return render(request, 'home/actions.html', {'questions': questions})
            else:
                messages.info(request,'password does not match')
        except Admin.DoesNotExist:
            messages.info(request,'Invalid username')
            return redirect('adminpage')

    return render(request, 'home/adminLogin.html')


def create_quiz(request):
    if request.method == 'POST':
        try: 
            q_text = request.POST.get('question')
            choices = request.POST.getlist('choices')
            correct_choice_index = request.POST.get('correct_choice')

            question = Question.objects.create(question=q_text)
            
            for index, c_text in enumerate(choices):
                is_correct = False
                if str(index) == correct_choice_index:
                    is_correct = True
                Choice.objects.create(choice_text=c_text, question=question, is_correct=is_correct)
            
            messages.success(request, 'Quiz created successfully!')
            return render(request, 'home/actions.html')

        except:
            messages.error(request, 'Failed to create quiz!')
            return render(request, 'home/actions.html')

    return render(request, 'home/createQuiz.html')


def update_quiz(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        try:
            for question in questions:
                new_q_text = request.POST.get(f'question_{question.id}')
                question.question = new_q_text
                question.save()
            
            new_choices = request.POST.getlist(f'choices_{question.id}')
            correct_choice_index = request.POST.get(f'correct_choice_{question.id}')

            #Clear previous choices
            Choice.objects.filter(question=question).delete()

            for index, choice_text in enumerate(new_choices):
                is_correct = str(index) == correct_choice_index
                Choice.objects.create(question=question, choice_text=choice_text, is_correct=is_correct)

            messages.success(request, "Quizzes updated successfully!")
            return render(request, 'home/actions.html')

        except:
            messages.error(request, 'Failed to update quiz!')
            return render(request, 'home/actions.html')

    return render(request, 'home/updateQuiz.html', {'questions': questions})


def delete_quiz(request):
    if request.method == 'POST':
        try:
            Choice.objects.all().delete()
            Question.objects.all().delete()
            messages.success(request, "Quiz has been deleted successfully!")
            return render(request, 'home/actions.html')
        except:
            messages.error(request, 'Failed to delete quiz!')
            return render(request, 'home/actions.html')
