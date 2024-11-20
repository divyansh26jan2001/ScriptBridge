from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import ProgrammingQuestion

# Create your views here.
def index_view(request):
    questions = ProgrammingQuestion.objects.all()
    return render(request,'ScriptBridgeWebApp/index.html',{'questions' : questions})
    # return HttpResponse("Hello World, Thanks")

def question_list_view(request):
    questions = ProgrammingQuestion.objects.all()
    return render(request,'ScriptBridgeWebApp/question_list.html',{'questions' : questions})

def about_us_view(request):
    return render(request,'ScriptBridgeWebApp/about_us.html')

def contact_us_view(request):
    return render(request,'ScriptBridgeWebApp/contact_us.html')


def view_solution(request, sr_no):
    # Get the specific question by sr_no
    question = get_object_or_404(ProgrammingQuestion, sr_no=sr_no)
    return render(request, 'ScriptBridgeWebApp/solution.html', {
        'question': question,
    })
