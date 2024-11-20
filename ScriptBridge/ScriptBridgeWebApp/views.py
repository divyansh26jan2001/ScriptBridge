from django.shortcuts import render,HttpResponse

# Create your views here.
def index_view(request):
    return render(request,'ScriptBridgeWebApp/index.html')
    # return HttpResponse("Hello World, Thanks")

def question_list_view(request):
    return render(request,'ScriptBridgeWebApp/question_list.html')

def about_us_view(request):
    return render(request,'ScriptBridgeWebApp/about_us.html')

def contact_us_view(request):
    return render(request,'ScriptBridgeWebApp/contact_us.html')