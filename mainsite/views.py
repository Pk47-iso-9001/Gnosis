from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def question(request):
    return render(request, 'question.html')

def entertainment(request):
    return render(request, 'entertainment.html')

def about(request):
    return render(request, 'about.html')


def physics(request):
    return render(request, 'physics.html')

def chemistry(request):
    return render(request, 'chemistry.html')

def mathematics(request):
    return render(request, 'mathematics.html')

def computer(request):
    return render(request, 'computer.html')

def biology(request):
    return render(request, 'biology.html')

def english(request):
    return render(request, 'english.html')

def nepali(request):
    return render(request, 'nepali.html')


def question_physics(request):
    return render(request, 'ques_phy.html')


def question_mathematics(request):
    return render(request, 'ques_math.html')

def question_computer(request):
    return render(request, 'ques_comp.html')


